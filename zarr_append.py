import xarray as xr

ds_nc = xr.open_dataset("20250102120000-REMSS-L4_GHRSST-SSTfnd-MW_OI-GLOB-v02.0-fv05.1.nc")
target = {"time": 1, "lon": 100, "lat": 100}
ds_nc.chunk(target).to_zarr("test.zarr", append_dim="time")

