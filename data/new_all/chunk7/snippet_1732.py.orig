#Source: https://stackoverflow.com/questions/59932201/filenotfounderror-errno-2-no-such-file-or-directory-c-users-dell-coil-2
original_dataset_dir=r"C:\Users\DELL\coil-20-unproc"
# Copy object1 images to train_obj1_dir
fnames = ['obj1_{}.png'.format(i) for i in range(0,72)]
for fname in fnames:
    src = os.path.join(original_dataset_dir, fname)
    dst = os.path.join(train_obj1_dir, fname)
    shutil.copyfile(src, dst)