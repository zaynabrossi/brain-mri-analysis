from pathlib import Path
import nibabel as nib
import matplotlib.pyplot as plt
project_folder = Path(__file__).resolve().parent.parent
data_path = project_folder/"data"/"example4d.nii.gz"
img=nib.load(str(data_path))
brain = img.get_fdata()
print(brain.shape)

volume = brain[:,:,:,0]
print("Voxel spacing:", tuple(round(float(x),2) for x in img.header.get_zooms()))
print(volume.shape)
print(img.affine)
print(nib.aff2axcodes(img.affine))

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
project_folder = Path(__file__).resolve().parent.parent
figures_folder = project_folder/"figures"
figures_folder.mkdir(exist_ok=True)
plt.savefig(figures_folder/"mri_orthogonal_views.png",
            dpi=300,bbox_inches="tight")
plt.show()


