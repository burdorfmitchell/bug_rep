from pyradiosky import SkyModel

sm = SkyModel()
sm.read_gleam_catalog("catalog_files/gleam.vot")
sm.write_skyh5("catalog_files/output.skyh5")
