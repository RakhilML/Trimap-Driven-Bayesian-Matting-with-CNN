#a rough implementation of the trimap generation algorithm
def generate_trimap(mask_path,eroision_iter=6,dilate_iter=8): #mask_path is the path to the mask image
    mask =  mask_path #cv2.imread(mask_path,0)
    mask = cv2.imread(mask,0)
    mask[mask==1] = 255
    d_kernel = np.ones((3,3))
    erode  = cv2.erode(mask,d_kernel,iterations=eroision_iter)
    dilate = cv2.dilate(mask,d_kernel,iterations=dilate_iter)
    unknown1 = cv2.bitwise_xor(erode,mask)
    unknown2 = cv2.bitwise_xor(dilate,mask)
    unknowns = cv2.add(unknown1,unknown2)
    unknowns[unknowns==255]=127
    trimap = cv2.add(mask,unknowns)
    cv2.imwrite("gandalf.png",mask)
    cv2.imwrite("dilate.png",dilate)
    cv2.imwrite("tri.png",trimap)
    labels = trimap.copy()
    labels[trimap==127]=1 #unknown
    labels[trimap==255]=2 #foreground
    cv2.imwrite(mask_path,labels)
    return labels

    plt.imshow(trimap,cmap='gray')
    plt.show()