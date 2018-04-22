"""Example files for use with niwidgets."""
__all__ = ['exampleatlas', 'examplezmap', 'examplet1',
           'examplesurface', 'exampleoverlays', 'streamlines']

# import pathlib & backwards compatibility
try:
    # on >3 this ships by default
    from pathlib import Path
except ModuleNotFoundError:
    # on 2.7 this should work
    try:
        from pathlib2 import Path
    except ModuleNotFoundError:
        raise ModuleNotFoundError('On python 2.7, niwidgets requires '
                                  'pathlib2 to be installed.')


root_dir = Path(__file__).parent / 'data'

exampleatlas = root_dir / 'cc400_roi_atlas.nii'
examplezmap = root_dir / 'cognitive control_pFgA_z.nii.gz'
examplet1 = root_dir / 'T1.nii.gz'

surface_dir = root_dir / 'example_surfaces'

examplesurface = surface_dir / 'lh.inflated'
exampleoverlays = {
    key: surface_dir / f
    for key, f in zip(['Area', 'Curvature', 'Thickness', 'Annotation'],
                      ('lh.area', 'lh.curv', 'lh.thickness', 'lh.aparc.annot'))
}

streamlines = root_dir / 'streamlines.trk'
