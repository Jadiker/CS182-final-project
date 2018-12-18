import rnn

# def main(train_model, generate_song, data_file, ckpt_file):
training_name = "dem_tweets"
how_many_tweets = 20
output_file = "test_output.txt"
prefix = " "

data_folder = "data"
models_folder = "models"
data_file = "{}/{}.txt".format(data_folder, training_name)
ckpt_file ="{}/{}/model.ckpt".format(models_folder, training_name)

rnn.generate_tweets(how_many_tweets, output_file, data_file, ckpt_file, prefix)
