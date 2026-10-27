#!/usr/bin/env python3
"""
Chuyen doi file Webcake (.pke) <-> JSON de AI (Codex, Claude) doc va sua duoc.

File .pke = base64( msgpack( du lieu trang ) ).

Cach dung:
  python pke_tool.py giai-nen  bo-me.pke            -> tao bo-me.json
  python pke_tool.py dong-goi  bo-me.json           -> tao bo-me.moi.pke
  python pke_tool.py liet-ke   bo-me.pke            -> in toan bo chu tren trang
  python pke_tool.py kiem-tra  bo-me.pke            -> kiem tra file hop le

Can cai: pip install msgpack
"""
import base64
import json
import sys
from pathlib import Path

import msgpack


def doc_pke(path):
    raw = Path(path).read_bytes().strip()
    return msgpack.unpackb(base64.b64decode(raw), raw=False, strict_map_key=False)


def ghi_pke(data, path):
    raw = base64.b64encode(msgpack.packb(data, use_bin_type=True))
    Path(path).write_bytes(raw)


def liet_ke_chu(data):
    """Tra ve danh sach (ten section, loai, id, noi dung chu)."""
    ket_qua = []

    def duyet(node, section):
        sp = node.get("specials", {})
        if "text" in sp:
            ket_qua.append((section, node.get("type"),
                            node.get("properties", {}).get("id"), sp["text"]))
        for c in node.get("children", []):
            duyet(c, section)

    for i, sec in enumerate(data["source"]["page"], 1):
        duyet(sec, f"Section {i}")
    for i, pop in enumerate(data["source"].get("popup", []), 1):
        duyet(pop, f"Popup {i}")
    return ket_qua


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    lenh, path = sys.argv[1], Path(sys.argv[2])

    if lenh == "giai-nen":
        data = doc_pke(path)
        out = path.with_suffix(".json")
        out.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"Da tao {out}")

    elif lenh == "dong-goi":
        data = json.loads(path.read_text(encoding="utf-8"))
        out = path.with_suffix(".moi.pke")
        ghi_pke(data, out)
        # tu kiem tra: doc lai phai ra dung du lieu vua ghi
        assert doc_pke(out) == data, "Loi: file dong goi khong khop du lieu"
        print(f"Da tao {out}")

    elif lenh == "liet-ke":
        for section, loai, id_, text in liet_ke_chu(doc_pke(path)):
            print(f"[{section}] {loai} ({id_}): {text}")

    elif lenh == "kiem-tra":
        raw = path.read_bytes().strip()
        data = doc_pke(path)
        lai = base64.b64encode(msgpack.packb(data, use_bin_type=True))
        src = data["source"]
        print("Tieu de :", src["settings"].get("title"))
        print("Section :", len(src["page"]), "| Popup:", len(src.get("popup", [])))
        print("Doc/ghi lai giong het file goc:", lai == raw)

    else:
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
