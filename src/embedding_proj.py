import os
import pandas as pd
from tensorboard.plugins.projector import visualize_embeddings
from tensorboard.plugins.projector.projector_config_pb2 import ProjectorConfig
import tensorflow as tf


base_path = "data/embedding"
conditions = ["untreated", "paclitaxel", "vorinostat"]

for condition in conditions:
    emb_path = os.path.join(base_path, conditions[0], "image_emd.tsv")
    df = pd.read_csv(emb_path, sep="\t")
    df.rename(columns={df.columns[0]: 0}, inplace=True)
    df = df.reset_index().rename(columns={"index": "protein"})

    df_mean = df.groupby(df.columns[0]).mean().reset_index()

    log_path = os.path.join(base_path, condition, "tensorboard", "projector")
    os.makedirs(log_path, exist_ok=True)

    df_mean.iloc[:, 1:].to_csv(os.path.join(log_path, "tensor.tsv"), sep="\t", index=False, header=False)
    df_mean["protein"].to_csv(os.path.join(log_path, "metadata.tsv"), sep="\t", index=False, header=False)

    embedding_values = df_mean.iloc[:, 1:].astype("float32").values
    embedding_var = tf.Variable(embedding_values, name="protein_embeddings")

    # Save model checkpoint
    ckpt = tf.train.Checkpoint(embedding=embedding_var)
    ckpt.save(os.path.join(log_path, "embedding.ckpt"))

    # Configure projector
    config = ProjectorConfig()
    embedding = config.embeddings.add()
    embedding.tensor_name = "embedding/.ATTRIBUTES/VARIABLE_VALUE"
    embedding.metadata_path = "metadata.tsv"

    visualize_embeddings(log_path, config)
