import struct

S = [
    "manifest",
    "package",
    "com.hossein.gallery",
    "application",
    "label",
    "گالری حسین",
    "activity",
    "name",
    ".MainActivity",
    "exported",
    "true",
    "intent-filter",
    "action",
    "android.intent.action.MAIN",
    "category",
    "android.intent.category.LAUNCHER",
    "android",
    "http://schemas.android.com/apk/res/android",
]

def ulen(n):
    return bytes([n]) if n < 128 else bytes([(n & 127) | 128, n >> 7])

def enc(s):
    b = s.encode("utf-8")
    u = len(s.encode("utf-16-le")) // 2
    return ulen(u) + ulen(len(b)) + b + b"\0"

offsets = []
pool = b""
for s in S:
    offsets.append(len(pool))
    pool += enc(s)

sp = struct.pack(
    "<HHIIIIII",
    0x0001, 28, 28 + 4*len(S) + len(pool),
    len(S), 0, 0x00000100,
    28 + 4*len(S), 0
)
sp += struct.pack("<" + "I"*len(S), *offsets) + pool

def node(t, body):
    size = 16 + len(body)
    return struct.pack("<HHIII", t, 16, size, 1, 0xFFFFFFFF) + body

def ns_start():
    return node(0x0100, struct.pack("<II", 16, 17))

def ns_end():
    return node(0x0101, struct.pack("<II", 16, 17))

def attr(ns, name, raw, typ, data):
    return struct.pack("<IIIIII", ns, name, raw, 8, 0, (typ << 24) | data)

def elem_start(ns, name, attrs):
    ext = struct.pack(
        "<IIHHHHHH",
        ns, name, 20, 20, len(attrs), 0, 0, 0
    )
    return node(0x0102, ext + b"".join(attrs))

def elem_end(ns, name):
    return node(0x0103, struct.pack("<II", ns, name))

ANDROID = 16
NO_NS = 0xFFFFFFFF
TYPE_STRING = 3
TYPE_BOOL = 0x12

chunks = [sp]

chunks.append(struct.pack("<HHI", 0x0180, 8, 8 + 4*len(S)) +
              struct.pack("<" + "I"*len(S), *[
                  0,
                  0,
                  0,
                  0,
                  0x01010001,
                  0,
                  0,
                  0x01010003,
                  0,
                  0x01010581,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0,
                  0
              ]))

chunks.append(ns_start())

chunks.append(elem_start(
    NO_NS, 0,
    [attr(NO_NS, 1, 2, TYPE_STRING, 2)]
))

chunks.append(elem_start(
    NO_NS, 3,
    [attr(ANDROID, 4, 5, TYPE_STRING, 5)]
))

chunks.append(elem_start(
    NO_NS, 6,
    [
        attr(ANDROID, 7, 8, TYPE_STRING, 8),
        attr(ANDROID, 9, 10, TYPE_BOOL, 1),
    ]
))

chunks.append(elem_start(NO_NS, 11, []))

chunks.append(elem_start(
    NO_NS, 12,
    [attr(ANDROID, 7, 13, TYPE_STRING, 13)]
))
chunks.append(elem_end(NO_NS, 12))

chunks.append(elem_start(
    NO_NS, 14,
    [attr(ANDROID, 7, 15, TYPE_STRING, 15)]
))
chunks.append(elem_end(NO_NS, 14))

chunks.append(elem_end(NO_NS, 11))
chunks.append(elem_end(NO_NS, 6))
chunks.append(elem_end(NO_NS, 3))
chunks.append(elem_end(NO_NS, 0))
chunks.append(ns_end())

body = b"".join(chunks)
header = struct.pack("<HHI", 0x0003, 8, 8 + len(body))

with open("build/AndroidManifest.xml", "wb") as f:
    f.write(header + body)

print("Manifest باینری ساخته شد")
