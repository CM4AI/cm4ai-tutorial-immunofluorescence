import os

from cellmaps_image_embedding.runner import DensenetEmbeddingGenerator
from cellmaps_image_embedding.runner import CellmapsImageEmbedder


input_base_path = "data/raw"
embedding_base_path = "data/embedding"

for treatment_folder in os.listdir(input_base_path):
    input_path = os.path.join(input_base_path, treatment_folder)
    embedding_path = os.path.join(embedding_base_path, treatment_folder)

    gen = DensenetEmbeddingGenerator(
        input_path,
        outdir=embedding_path,
        model_path="https://github.com/CellProfiling/densenet/releases/download/v0.1.0/external_crop512_focal_slov_hardlog_class_densenet121_dropout_i768_aug2_5folds_fold0_final.pth",
        fold=1
    )
    embedder = CellmapsImageEmbedder(
        outdir=embedding_path,
        inputdir=input_path,
        embedding_generator=gen,
        name=f"{treatment_folder} IF Embedding",
        organization_name="CM4AI",
        project_name="CM4AI IF Embedding Tutorial"
    )
    embedder.run()
