"""Design IR: the tool-independent representation the engines work on.

Coordinates are in millimetres in the KiCad board frame (x right, y down).
Rotation follows KiCad: a positive angle turns a local offset (x, y) into
(x*cos + y*sin, -x*sin + y*cos).
"""

from __future__ import annotations

import math
import re
from dataclasses import dataclass, field

GROUND_NET = re.compile(r"^/?(A|D|P|S)?(GND|VSS|GROUND)\w*$", re.IGNORECASE)
POWER_NET = re.compile(
    r"^/?(\+?\d+V\d*|\+?\d+V|V?\d+V\d+|VCC\w*|VDD\w*|VBUS\w*|VBAT\w*|VIN\w*|VSYS\w*|\+\w+)$",
    re.IGNORECASE,
)
EXTERNAL_CONNECTOR = re.compile(
    r"(USB|Jack|Barrel|RJ\d|Terminal|DSUB|D-Sub|DB\d|SMA|BNC|Phoenix|Molex|JST|Audio)",
    re.IGNORECASE,
)

KIND_BY_PREFIX = [
    ("USB", "connector"),
    ("LED", "led"),
    ("FID", "fiducial"),
    ("MH", "mounting"),
    ("SW", "switch"),
    ("TP", "testpoint"),
    ("CN", "connector"),
    ("IC", "ic"),
    ("FB", "inductor"),
    ("C", "capacitor"),
    ("R", "resistor"),
    ("L", "inductor"),
    ("D", "diode"),
    ("Q", "transistor"),
    ("U", "ic"),
    ("J", "connector"),
    ("P", "connector"),
    ("Y", "crystal"),
    ("X", "crystal"),
    ("H", "mounting"),
    ("F", "fuse"),
    ("K", "relay"),
    ("T", "transformer"),
    ("V", "tube"),
]


def classify_ref(ref: str) -> str:
    prefix = re.match(r"^[A-Za-z_]+", ref)
    if not prefix:
        return "other"
    p = prefix.group(0).upper()
    for key, kind in KIND_BY_PREFIX:
        if p == key or (len(key) > 1 and p.startswith(key)):
            return kind
    return "other"


def net_role(name: str | None) -> str:
    if not name:
        return "none"
    base = name.split("/")[-1]
    if GROUND_NET.match(base):
        return "ground"
    if POWER_NET.match(base):
        return "power"
    return "signal"


def rotate(dx: float, dy: float, deg: float) -> tuple[float, float]:
    a = math.radians(deg)
    c, s = math.cos(a), math.sin(a)
    return dx * c + dy * s, -dx * s + dy * c


@dataclass
class Pad:
    number: str
    net: str | None
    dx: float  # offset from the component origin, in the rotation-0 frame
    dy: float


@dataclass
class Component:
    ref: str
    value: str
    footprint: str
    x: float
    y: float
    rotation: float  # degrees, absolute
    flipped: bool
    locked: bool
    has_through_hole: bool
    bbox: tuple[float, float, float, float]  # minx, miny, maxx, maxy in the rotation-0 frame
    pads: list[Pad] = field(default_factory=list)
    kind: str = "other"

    def pad_position(self, pad: Pad, x: float | None = None, y: float | None = None,
                     rotation: float | None = None) -> tuple[float, float]:
        ox = self.x if x is None else x
        oy = self.y if y is None else y
        rot = self.rotation if rotation is None else rotation
        rx, ry = rotate(pad.dx, pad.dy, rot)
        return ox + rx, oy + ry

    def nets(self) -> set[str]:
        return {p.net for p in self.pads if p.net}


@dataclass
class Net:
    name: str
    pins: list[tuple[int, int]]  # (component index, pad index)
    role: str = "signal"


@dataclass
class Board:
    bbox: tuple[float, float, float, float]  # minx, miny, maxx, maxy
    copper_layers: int
    # Allowed-area raster: mask[iy][ix] is True where a point is inside the outline.
    mask_origin: tuple[float, float] = (0.0, 0.0)
    mask_pitch: float = 0.5
    mask: list[list[bool]] = field(default_factory=list)
    # Fixed copper items outside footprints (texts, logos, keepouts):
    # (minx, miny, maxx, maxy, side, label) with side 0 = front, 1 = back, 2 = inner layer
    # (blocks through-hole parts only), 3 = every side (footprint keepout).
    obstacles: list[tuple[float, float, float, float, int, str]] = field(default_factory=list)
    # Routing resources for the congestion model.
    routing_layers: int = 2  # copper layers available for tracks (inner plane layers excluded)
    track_pitch_mm: float = 0.5  # default track width + clearance (at least the board minimums)
    pour_nets: list[str] = field(default_factory=list)  # nets carried by a copper pour

    def inside(self, x: float, y: float) -> bool:
        if not self.mask:
            minx, miny, maxx, maxy = self.bbox
            return minx <= x <= maxx and miny <= y <= maxy
        ix = int((x - self.mask_origin[0]) / self.mask_pitch)
        iy = int((y - self.mask_origin[1]) / self.mask_pitch)
        if iy < 0 or iy >= len(self.mask) or ix < 0 or ix >= len(self.mask[0]):
            return False
        return self.mask[iy][ix]


@dataclass
class DesignIR:
    name: str
    components: list[Component]
    nets: list[Net]
    board: Board
    source_path: str = ""

    def index(self) -> dict[str, int]:
        return {c.ref: i for i, c in enumerate(self.components)}

    def net_by_name(self) -> dict[str, Net]:
        return {n.name: n for n in self.nets}
