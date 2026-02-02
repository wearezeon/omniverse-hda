# Fusion → Houdini → Omniverse Physics Pipeline

Automatic enrichment of Fusion-exported USD files with physical material properties for Omniverse.

## Files
- `material_physics_lookup.json` - Material properties database
- `enrich_physics.py` - Houdini Python LOP script

## Usage
1. Load Fusion USDZ in Houdini LOP
2. Add Python LOP node with enrich_physics.py code
3. Cook and export USD
4. Open in Omniverse
