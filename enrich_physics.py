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
                api = UH\HHR’ÒT€€€€€€€€€…Á¤€ôU    )•…Ñ••¹Í¥ÑåÑÑÈ¡ÁÉ½ÁÍl‰‘•¹Í¥Ñä‰t¤(€€€€€€€€€€€€€€€…Á¤¹É•…Ñ•MÑ…Ñ¥É¥Ñ¥½¹ÑÑÈ¡ÁÉ½ÁÍl‰ÍÑ…Ñ¥É¥Ñ¥½¸‰t¤(€€€€€€€€€€€€€€€…Á¤¹É•…Ñ•å¹…µ¥É¥Ñ¥½¹ÑÑÈ¡ÁÉ½ÁÍl‰‘å¹…µ¥É¥Ñ¥½¸["dynamicFrictionÈ™[˜[ZXÑœšXİ[Û…²&G–æÖ–4g&–7F–öál‰‘å·F—GWF–öâ%Ò¢&–çB†b$Æ–VB‡—6–72Fò¶æÖWÒ" ¦Ö–â‚ 