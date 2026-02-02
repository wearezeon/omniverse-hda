"""Houdini Python LOP: Enrich USD Materials with Physics Properties"""
from pxr import Usd, UsdShade, UsdPhysics
import json, re, os

LOOKUP_PATH = "$HIP/material_physics_lookup.json"
FUSION_PATTERN = r"XID_([A-Za-z0-9]+)_[A-F0-9]+"

def extract_material_name(name, pattern=FUSION_PATTERN):
    match = re.match(pattern, name)
    return match.group(1) if match else name

def main():
    node = hou.pwd()
    stage = node.editableStage()
    path = hou.expandString(LOOKUP_PATH)
    with open(path) as f:
        lookup = json.load(f)
    for prim in stage.Traverse():
        if prim.IsA(UsdShade.Material):
            name = extract_material_name(prim.GetName())
            if name in lookup:
                props = lookup[name]
                api = UsdPhysics.MaterialAPI.Apply(prim)
                api.CreateDensityAttr(props["density"])
                api.CreateStaticFrictionAttr(props["staticFriction"])
                api.CreateDynamicFrictionAttr(props["dynamicFriction"])
                api.CreateRestitutionAttr(props["restitution"])
                print(f"Applied physics to {name}")

main()
