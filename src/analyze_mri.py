from pathlib import Path
import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt
project_folder = Path(__file__).resolve().parent.parent
data_path = project_folder/"data"/"example4d.nii.gz"
img=nib.load(str(data_path))
brain = img.get_fdata()
print("Brain shape:", (brain.shape)) 

volume = brain[:,:,:,0]
nonzero_voxels = volume[volume>0]
total_voxels = volume.size
nonzero_count= nonzero_voxels.size
nonzero_percentage = (nonzero_count/total_voxels)*100
print("Minimum intensity:", np.min(volume))
print("Maximum intensity:", np.max(volume))
print("Mean intensity:", round(np.mean(volume),2))
print("Nonzero mean:", round(np.mean(nonzero_voxels),2))
print("Standard deviation:", round(np.std(volume),2))
print("\nVoxel spacing:", tuple(round(float(x),2) for x in img.header.get_zooms()))
print("Total voxels:", total_voxels)
print("Nonzero voxels:", nonzero_count)
print("Nonzero percentage:", round(nonzero_percentage,2), "%")
print(volume.shape)
print(((np.array2string(img.affine, formatter={'float_kind': lambda x:f'{x:.2e}'}))))
print(nib.aff2axcodes(img.affine))

plt.figure(figsize=(8,5))
plt.hist(nonzero_voxels, bins=50)
plt.xlabel("Voxel intensity")
plt.ylabel("Number of voxels")
plt.title("MRI Intensity Distribution")
plt.tight_layout()
project_folder = Path(__file__).resolve().parent.parent
figures_folder = project_folder/"figures"
figures_folder.mkdir(exist_ok=True)
plt.savefig(
    figures_folder /"mri_intensity_histogram.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()

middle_slice = volume[:,:,12]
#plt.imshow(middle_slice, cmap="gray")
#plt.title("MRI - Slice 12")
#plt.colorbar()
#plt.show()

fig, axes = plt.subplots(1,3, figsize=(12,4))
axes[0].imshow(volume[64,:,:], cmap="gray",
               aspect=2.0/2.2)
axes[0].set_title("Sagittal")
axes[1].imshow(volume[:,48,:], cmap="gray",
               aspect=2.0/2.2)
axes[1].set_title("Coronal")
axes[2].imshow(volume[:,:,12], cmap="gray",
               aspect=2.0/2.0)
axes[2].set_title("Axial")
plt.tight_layout()
plt.savefig(figures_folder/"mri_orthogonal_views.png",
            dpi=300,bbox_inches="tight")
plt.close()

