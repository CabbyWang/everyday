***
````
import dicom
import pydicom
````
（在0.9.9版本以前使用dicom， 在之后的1.0版本之后使用pydicom）

ds = dicom.read_file("d:\\test\\101.dcm")   #读取dicom文件

ds["PatientsSex"]   或 ds[0x0010, 0x0040] (16进制)   #获取某一个属性, 【一整行】如下
                                   (0010, 0040) Patient's Sex      CS: 'F'
#获取具体值，作如下操作
data_element = ds.data_element('PatientsSex')  # or data_element = ds[0x0010, 0x0040]
print(data_element.VR, data_element.value)
【out】'CS'  'F'

del ds.SoftwareVersions      #删除属性SoftwareVersions

pixel_bytes = ds.PixelData   #原始的二进制文件

pix = ds.pixel_array         #CT值组成了一个矩阵

ds.save_as('d:\\test\\101.dcm')   #写入操作，保存

ds.file_meta.MediaStorageSOPClassUID = ''
ds.file_meta.FileMetaInformationVersion = ''
ds.file_meta.File.MetaInformationGroupLength = ''
ds.file_meta.ImplementationClassUID = ''
ds.file_meta.MediaStorageSOPInstanceUID = ''

[nibable解析nii]http://nipy.org/nibabel/
