import os

from cellmaps_imagedownloader.runner import CM4AICopyDownloader
from cellmaps_imagedownloader.runner import CellmapsImageDownloader
from cellmaps_imagedownloader.gene import CM4AITableConverter
from cellmaps_imagedownloader.gene import ImageGeneNodeAttributeGenerator
from cellmaps_imagedownloader.proteinatlas import CM4AIImageCopyTupleGenerator

from cellmaps_image_embedding.runner import DensenetEmbeddingGenerator
from cellmaps_image_embedding.runner import CellmapsImageEmbedder

input_base_path = "data/raw"
embedding_base_path = "data/embedding"

for treatment_folder in os.listdir(input_base_path):
    input_path = os.path.join(input_base_path, treatment_folder)
    manifest_path = os.path.join(input_path, "manifest.csv")
    embedding_path = os.path.join(embedding_base_path, treatment_folder)

    converter = CM4AITableConverter(cm4ai=manifest_path)
    samples_list, unique_list = converter.get_samples_and_unique_lists()
    dloader = CM4AICopyDownloader()

    imagegen = ImageGeneNodeAttributeGenerator(unique_list=unique_list, samples_list=samples_list)
    imageurlgen = CM4AIImageCopyTupleGenerator(samples_list=imagegen.get_samples_list())
    downloader = CellmapsImageDownloader(
        outdir=input_path,
        existing_outdir=False,
        imagedownloader=dloader,
        imgsuffix="jpg",
        imagegen=imagegen,
        imageurlgen=imageurlgen
    )
    downloader.run()

    # gen = DensenetEmbeddingGenerator(
    #     input_path,
    #     outdir=embedding_path,
    #     model_path="https://github.com/CellProfiling/densenet/releases/download/v0.1.0/external_crop512_focal_slov_hardlog_class_densenet121_dropout_i768_aug2_5folds_fold0_final.pth",
    #     fold=1
    # )
    # embedder = CellmapsImageEmbedder(
    #     outdir=embedding_path,
    #     inputdir=input_path,
    #     embedding_generator=gen,
    #     name=f"{treatment_folder} IF Embedding",
    #     organization_name="CM4AI",
    #     project_name="CM4AI IF Embedding Tutorial"
    # )
    # embedder.run()
