import tensorflow as tf
import tensorflow_datasets as tfds

builders = tfds.list_builders()

print (builders)

'''
['abstract_reasoning', 'aeslc', 'aflw2k3d', 'amazon_us_reviews', 'arc', 
'bair_robot_pushing_small', 'beans', 'big_patent', 'bigearthnet', 'billsum', 'binarized_mnist', 
'binary_alpha_digits', 'blimp', 'c4', 'caltech101', 'caltech_birds2010', 'caltech_birds2011', 'cars196', 
'cassava', 'cats_vs_dogs', 'celeb_a', 'celeb_a_hq', 'cfq', 'chexpert', 'cifar10', 'cifar100', 'cifar10_1', 
'cifar10_corrupted', 'citrus_leaves', 'cityscapes', 'civil_comments', 'clevr', 'cmaterdb', 'cnn_dailymail', 
'coco', 'coil100', 'colorectal_histology', 'colorectal_histology_large', 'common_voice', 'cos_e', 'crema_d', 
'curated_breast_imaging_ddsm', 'cycle_gan', 'deep_weeds', 'definite_pronoun_resolution', 'dementiabank', 
'diabetic_retinopathy_detection', 'div2k', 'dmlab', 'downsampled_imagenet', 'dsprites', 'dtd', 'duke_ultrasound', 
'emnist', 'eraser_multi_rc', 'esnli', 'eurosat', 'fashion_mnist', 'flic', 'flores', 'food101', 'forest_fires', 
'gap', 'geirhos_conflict_stimuli', 'german_credit_numeric', 'gigaword', 'glue', 'groove', 'higgs', 
'horses_or_humans', 'i_naturalist2017', 'image_label_folder', 'imagenet2012', 'imagenet2012_corrupted', 
'imagenet2012_subset', 'imagenet_resized', 'imagenette', 'imagewang', 'imdb_reviews', 'iris', 'kitti', 'kmnist', 
'lfw', 'librispeech', 'librispeech_lm', 'libritts', 'ljspeech', 'lm1b', 'lost_and_found', 'lsun', 'malaria', 
'math_dataset', 'mnist', 'mnist_corrupted', 'movie_rationales', 'moving_mnist', 'multi_news', 'multi_nli', 
'multi_nli_mismatch', 'natural_questions', 'newsroom', 'nsynth', 'omniglot', 'open_images_challenge2019_detection', 
'open_images_v4', 'opinosis', 'oxford_flowers102', 'oxford_iiit_pet', 'para_crawl', 'patch_camelyon', 'pet_finder', 
'places365_small', 'plant_leaves', 'plant_village', 'plantae_k', 'qa4mre', 'quickdraw_bitmap', 'reddit', 'reddit_tifu', 
'resisc45', 'robonet', 'rock_paper_scissors', 'rock_you', 'samsum', 'savee', 'scan', 'scene_parse150', 'scicite', 
'scientific_papers', 'shapes3d', 'smallnorb', 'snli', 'so2sat', 'speech_commands', 'squad', 'stanford_dogs', 
'stanford_online_products', 'starcraft_video', 'stl10', 'sun397', 'super_glue', 'svhn_cropped', 
'ted_hrlr_translate', 'ted_multi_translate', 'tedlium', 'tf_flowers', 'the300w_lp', 'tiny_shakespeare', 
'titanic', 'trivia_qa', 'uc_merced', 'ucf101', 'vgg_face2', 'visual_domain_decathlon', 'voc', 'voxceleb', 
'waymo_open_dataset', 'web_questions', 'wider_face', 'wiki40b', 'wikihow', 'wikipedia', 'wmt14_translate', 
'wmt15_translate', 'wmt16_translate', 'wmt17_translate', 'wmt18_translate', 'wmt19_translate', 'wmt_t2t_translate',
 'wmt_translate', 'xnli', 'xsum', 'yelp_polarity_reviews']
'''

data, info = tfds.load("mnist", with_info=True)
train_data, test_data = data['train'], data['test']

print(info)

'''
tfds.core.DatasetInfo(
    name='mnist',
    version=3.0.1,
    description='The MNIST database of handwritten digits.',
    homepage='http://yann.lecun.com/exdb/mnist/',
    features=FeaturesDict({
        'image': Image(shape=(28, 28, 1), dtype=tf.uint8),
        'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=10),
    }),
    total_num_examples=70000,
    splits={
        'test': 10000,
        'train': 60000,
    },
    supervised_keys=('image', 'label'),
    citation="""@article{lecun2010mnist,
      title={MNIST handwritten digit database},
      author={LeCun, Yann and Cortes, Corinna and Burges, CJ},
      journal={ATT Labs [Online]. Available: http://yann. lecun. com/exdb/mnist},
      volume={2},
      year={2010}
    }""",
    redistribution_info=,
)
'''