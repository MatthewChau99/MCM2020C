import random
import sys
import time

import numpy as np
import pandas as pd

# Initializing global variables
data_cluster_map = {}
cluster_data_map = {}
input_file = sys.argv[1]
num_clusters = int(sys.argv[2])
output_file_name = sys.argv[3]

df = pd.read_csv(input_file, sep=',', index_col=0)
df = df.transpose()
print(df)

for i in range(len(df)):
    data_cluster_map.update({i: 0})

for i in range(num_clusters):
    cluster_data_map.update({i: set()})


# Finds the average of a list of tuples(vector)
def tuple_average(tup_list):        # O (# of cols)
    return tuple([np.average([tup[idx] for tup in tup_list]) for idx in range(1, min([len(t) for t in tup_list]))])


# Finds the euclidean distance of two tuples(vector)
def euclidean_dist(tup1, tup2):         # O (# of cols)
    return np.sqrt(sum([(tup1[idx] - tup2[idx]) ** 2 for idx in range(1, min(len(tup1), len(tup2)))]))


# Clusters the dataset into k clusters
def k_means(k):
    centroids_index = random.sample(range(len(df)), k)
    centroids_index = [df.index[index] for index in centroids_index]
    centroids = [tuple(df.loc[index]) for index in centroids_index]
    change = True
    count = 0
    sum_squared_error = 0
    silhouette_coeff = 0
    while change:
        change = False
        print(count)
        for idx in df.index:        # O(# of words)
            dist_from_centroids = []
            for centroid in centroids:      # O(# of cols)
                dist_from_centroids.append(euclidean_dist(tuple(df.loc[idx]), centroid))

            cluster_idx = dist_from_centroids.index(min(dist_from_centroids))

            # Updating data -> cluster map
            old_cluster_idx = data_cluster_map.get(idx)
            if cluster_idx != old_cluster_idx:
                change = True  # The clusters have changed
                data_cluster_map.update({idx: cluster_idx})

            # Updating cluster -> data map
            # Removing from old cluster
            if count >= 1:
                data_in_cluster = cluster_data_map.get(old_cluster_idx)
                data_in_cluster.remove(idx)
                cluster_data_map.update({old_cluster_idx: data_in_cluster})
            # Adding to new cluster
            data_in_cluster = cluster_data_map.get(cluster_idx)
            data_in_cluster.add(idx)
            cluster_data_map.update(
                {cluster_idx: data_in_cluster})

        # Updating centroids
        for idx in range(len(centroids)):       # O(# of cols)
            centroids[idx] = tuple_average([df.loc[cluster_data] for cluster_data in cluster_data_map.get(idx)])

        count += 1


start_time = time.time()
k_means(num_clusters)
print("--- %s seconds ---" % (time.time() - start_time))

output_file = open(output_file_name, 'w')
for i in range(len(cluster_data_map)):
    cluster = cluster_data_map.get(i)
    output_file.write('-------------------- Cluster %d --------------------\n' % i)
    for word in cluster:
        output_file.write("%s\n" % word)
    output_file.write('\n\n')
output_file.close()
