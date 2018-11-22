from modules.storage import Storage
from concurrent.futures import ProcessPoolExecutor, as_completed
from modules.utils import Utils

saved_episodes = Storage.load_pickle('storage/wr.pkl')

utils = Utils()

with ProcessPoolExecutor(max_workers=4) as executor:
    futures = [ executor.submit(utils.get_episode_escuchas, episode) for episode in saved_episodes ]
    results = []
    for completed_futures in as_completed(futures):
        results.append(completed_futures.result())
    Storage.save_csv(filename='storage/wr.csv', data=results)