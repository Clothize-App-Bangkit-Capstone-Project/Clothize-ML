import os
import csv

DATA_PATH = os.path.join('..', 'aug_data')

FIELDS = ['image', 'label']

train_csv = os.path.join(DATA_PATH, 'train.csv')
validation_csv = os.path.join(DATA_PATH, 'validation.csv')

train_path = os.path.join(DATA_PATH, 'train')
val_path = os.path.join(DATA_PATH, 'val')

train_images_path = os.listdir(os.path.join(train_path, 'images'))
train_images = [ os.path.join(train_path, 'images', image) for image in train_images_path ]
train_label_path = os.listdir(os.path.join(train_path, 'labels'))
train_labels = [ os.path.join(train_path, 'labels', label) for label in train_label_path ]

val_images_path = os.listdir(os.path.join(val_path, 'images'))
val_images = [ os.path.join(val_path, 'images', image) for image in val_images_path ]
val_label_path = os.listdir(os.path.join(val_path, 'labels'))
val_labels = [ os.path.join(val_path, 'labels', label) for label in val_label_path ]

train = [{'image' : image, 'label' : label} for image, label in zip(train_images, train_labels)]
val = [{'image' : image, 'label' : label} for image, label in zip(val_images, val_labels)]

print(train[0])
print(val[0])

with open(train_csv, 'w') as f :
    writer = csv.DictWriter(f, fieldnames=train[0].keys())
    writer.writeheader()
    writer.writerows(train)

with open(validation_csv, 'w') as f :
    writer = csv.DictWriter(f, fieldnames=val[0].keys())
    writer.writeheader()
    writer.writerows(val)

