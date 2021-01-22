import re
import unittest
from ir_datasets.datasets.codesearchnet import CodeSearchNetDoc, CodeSearchNetChallengeQrel
from ir_datasets.formats import GenericDoc, GenericQuery, TrecQrel
from .base import DatasetIntegrationTest


class TestCodeSearchNet(DatasetIntegrationTest):
    def test_codesearchnet_docs(self):
        self._test_docs('codesearchnet', count=2070536, items={
            0: CodeSearchNetDoc('https://github.com/soimort/you-get/blob/b746ac01c9f39de94cac2d56f665285b0523b974/src/you_get/extractors/youtube.py#L135-L143', 'soimort/you-get', 'src/you_get/extractors/youtube.py', 'YouTube.get_vid_from_url', re.compile('^def get_vid_from_url\\(url\\):\n        """Extracts video ID from URL\\.\n        """\n        return match1\\(.{210}      parse_query_param\\(url, \'v\'\\) or \\\\\n          parse_query_param\\(parse_query_param\\(url, \'u\'\\), \'v\'\\)$', flags=48), 'python'),
            9: CodeSearchNetDoc('https://github.com/soimort/you-get/blob/b746ac01c9f39de94cac2d56f665285b0523b974/src/you_get/extractors/sina.py#L54-L64', 'soimort/you-get', 'src/you_get/extractors/sina.py', 'sina_download_by_vkey', re.compile('^def sina_download_by_vkey\\(vkey, title=None, output_dir=\'\\.\', merge=True, info_only=False\\):\n    """Dow.{229} info_only:\n        download_urls\\(\\[url\\], title, \'flv\', size, output_dir = output_dir, merge = merge\\)$', flags=48), 'python'),
            2070535: CodeSearchNetDoc('https://github.com/christophehurpeau/SpringbokJS/blob/bc1069baafc0785d361a33ff5a2fa604b8b3b454/src/browser/base/S.History.js#L72-L78', 'christophehurpeau/SpringbokJS', 'src/browser/base/S.History.js', '', re.compile('^function\\(fragmentOverride,state\\)\\{\n\\\t\\\t\\\tvar fragment = baseUrl\\+\\( this\\.fragment = this\\.getFragment\\(fragm.{32}\\\t\\\t\\\t\\\tvar a=\\$\\(\'a\\[href="\'\\+fragment\\+\'"\\]\'\\);\n\\\t\\\t\\\t\\\ta\\.length===0 \\? S\\.redirect\\(fragment\\) : a\\.click\\(\\);\n\\\t\\\t\\\t\\}\n\\\t\\\t\\}$', flags=48), 'javascript'),
        })

    def test_codesearchnet_queries(self):
        self._test_queries('codesearchnet/train', count=1880853, items={
            0: GenericQuery('https://github.com/ageitgey/face_recognition/blob/c96b010c02f15e8eeb0f71308c641179ac1f19bb/examples/face_recognition_knn.py#L46-L108', 'Trains a k-nearest neighbors classifier for face recognition.\n\n    :param train_dir: directory that contains a sub-directory for each known person, with its name.\n\n     (View in source code to see train_dir example tree structure)\n\n     Structure:\n        <train_dir>/\n        ├── <person1>/\n        │   ├── <somename1>.jpeg\n        │   ├── <somename2>.jpeg\n        │   ├── ...\n        ├── <person2>/\n        │   ├── <somename1>.jpeg\n        │   └── <somename2>.jpeg\n        └── ...\n\n    :param model_save_path: (optional) path to save model on disk\n    :param n_neighbors: (optional) number of neighbors to weigh in classification. Chosen automatically if not specified\n    :param knn_algo: (optional) underlying data structure to support knn.default is ball_tree\n    :param verbose: verbosity of training\n    :return: returns knn classifier that was trained on the given data.'),
            9: GenericQuery('https://github.com/ageitgey/face_recognition/blob/c96b010c02f15e8eeb0f71308c641179ac1f19bb/face_recognition/api.py#L135-L151', "Returns an 2d array of bounding boxes of human faces in a image using the cnn face detector\n    If you are using a GPU, this can give you much faster results since the GPU\n    can process batches of images at once. If you aren't using a GPU, you don't need this function.\n\n    :param img: A list of images (each as a numpy array)\n    :param number_of_times_to_upsample: How many times to upsample the image looking for faces. Higher numbers find smaller faces.\n    :param batch_size: How many images to include in each GPU processing batch.\n    :return: A list of tuples of found face locations in css (top, right, bottom, left) order"),
            1880852: GenericQuery('https://github.com/nutella-framework/nutella_lib.js/blob/b3a3406a407e2a1ada6edcc503b70991f9cb249b/src/run_net_bin.js#L87-L102', 'Helper function This function uploads a file with a certain file name. If the upload is successful the first callback is executed, otherwise the second one is.'),
        })
        self._test_queries('codesearchnet/valid', count=89154, items={
            0: GenericQuery('https://github.com/openai/baselines/blob/3301089b48c42b87b396e246ea3f56fa4bfc9678/baselines/deepq/deepq.py#L95-L333', 'Train a deepq model.\n\n    Parameters\n    -------\n    env: gym.Env\n        environment to train on\n    network: string or a function\n        neural network to use as a q function approximator. If string, has to be one of the names of registered models in baselines.common.models\n        (mlp, cnn, conv_only). If a function, should take an observation tensor and return a latent variable tensor, which\n        will be mapped to the Q function heads (see build_q_func in baselines.deepq.models for details on that)\n    seed: int or None\n        prng seed. The runs with the same seed "should" give the same results. If None, no seeding is used.\n    lr: float\n        learning rate for adam optimizer\n    total_timesteps: int\n        number of env steps to optimizer for\n    buffer_size: int\n        size of the replay buffer\n    exploration_fraction: float\n        fraction of entire training period over which the exploration rate is annealed\n    exploration_final_eps: float\n        final value of random action probability\n    train_freq: int\n        update the model every `train_freq` steps.\n        set to None to disable printing\n    batch_size: int\n        size of a batched sampled from replay buffer for training\n    print_freq: int\n        how often to print out training progress\n        set to None to disable printing\n    checkpoint_freq: int\n        how often to save the model. This is so that the best version is restored\n        at the end of the training. If you do not wish to restore the best version at\n        the end of the training set this variable to None.\n    learning_starts: int\n        how many steps of the model to collect transitions for before learning starts\n    gamma: float\n        discount factor\n    target_network_update_freq: int\n        update the target network every `target_network_update_freq` steps.\n    prioritized_replay: True\n        if True prioritized replay buffer will be used.\n    prioritized_replay_alpha: float\n        alpha parameter for prioritized replay buffer\n    prioritized_replay_beta0: float\n        initial value of beta for prioritized replay buffer\n    prioritized_replay_beta_iters: int\n        number of iterations over which beta will be annealed from initial value\n        to 1.0. If set to None equals to total_timesteps.\n    prioritized_replay_eps: float\n        epsilon to add to the TD errors when updating priorities.\n    param_noise: bool\n        whether or not to use parameter space noise (https://arxiv.org/abs/1706.01905)\n    callback: (locals, globals) -> None\n        function called at every steps with state of the algorithm.\n        If callback returns true training stops.\n    load_path: str\n        path to load the model from. (default: None)\n    **network_kwargs\n        additional keyword arguments to pass to the network builder.\n\n    Returns\n    -------\n    act: ActWrapper\n        Wrapper over act function. Adds ability to save it and load it.\n        See header of baselines/deepq/categorical.py for details on the act function.'),
            9: GenericQuery('https://github.com/openai/baselines/blob/3301089b48c42b87b396e246ea3f56fa4bfc9678/baselines/common/cmd_util.py#L21-L52', 'Create a wrapped, monitored SubprocVecEnv for Atari and MuJoCo.'),
            89153: GenericQuery('https://github.com/christophehurpeau/SpringbokJS/blob/bc1069baafc0785d361a33ff5a2fa604b8b3b454/src/browser/base/S.History.js#L72-L78', 'Attempt to load the current URL fragment.'),
        })
        self._test_queries('codesearchnet/test', count=100529, items={
            0: GenericQuery('https://github.com/soimort/you-get/blob/b746ac01c9f39de94cac2d56f665285b0523b974/src/you_get/extractors/youtube.py#L135-L143', 'Extracts video ID from URL.'),
            9: GenericQuery('https://github.com/soimort/you-get/blob/b746ac01c9f39de94cac2d56f665285b0523b974/src/you_get/extractors/sina.py#L54-L64', 'Downloads a Sina video by its unique vkey.\n    http://video.sina.com/'),
            100528: GenericQuery('https://github.com/dherges/grunt-bower-event/blob/ce7dc2303ef186ccf5eaa8d5b691102e13523076/tasks/lib/BowerTask.js#L24-L30', "Creates a new task.\n\n@param context Task function context (='this' inside a grunt task function)\n@param grunt Grunt object"),
        })
        self._test_queries('codesearchnet/challenge', count=99, items={
            0: GenericQuery('1', 'convert int to string'),
            9: GenericQuery('10', 'binomial distribution'),
            98: GenericQuery('99', 'how to read .csv file in an efficient way?'),
        })

    def test_codesearchnet_qrels(self):
        self._test_qrels('codesearchnet/train', count=1880853, items={
            0: TrecQrel('https://github.com/ageitgey/face_recognition/blob/c96b010c02f15e8eeb0f71308c641179ac1f19bb/examples/face_recognition_knn.py#L46-L108', 'https://github.com/ageitgey/face_recognition/blob/c96b010c02f15e8eeb0f71308c641179ac1f19bb/examples/face_recognition_knn.py#L46-L108', 1, '0'),
            9: TrecQrel('https://github.com/ageitgey/face_recognition/blob/c96b010c02f15e8eeb0f71308c641179ac1f19bb/face_recognition/api.py#L135-L151', 'https://github.com/ageitgey/face_recognition/blob/c96b010c02f15e8eeb0f71308c641179ac1f19bb/face_recognition/api.py#L135-L151', 1, '0'),
            1880852: TrecQrel('https://github.com/nutella-framework/nutella_lib.js/blob/b3a3406a407e2a1ada6edcc503b70991f9cb249b/src/run_net_bin.js#L87-L102', 'https://github.com/nutella-framework/nutella_lib.js/blob/b3a3406a407e2a1ada6edcc503b70991f9cb249b/src/run_net_bin.js#L87-L102', 1, '0'),
        })
        self._test_qrels('codesearchnet/valid', count=89154, items={
            0: TrecQrel('https://github.com/openai/baselines/blob/3301089b48c42b87b396e246ea3f56fa4bfc9678/baselines/deepq/deepq.py#L95-L333', 'https://github.com/openai/baselines/blob/3301089b48c42b87b396e246ea3f56fa4bfc9678/baselines/deepq/deepq.py#L95-L333', 1, '0'),
            9: TrecQrel('https://github.com/openai/baselines/blob/3301089b48c42b87b396e246ea3f56fa4bfc9678/baselines/common/cmd_util.py#L21-L52', 'https://github.com/openai/baselines/blob/3301089b48c42b87b396e246ea3f56fa4bfc9678/baselines/common/cmd_util.py#L21-L52', 1, '0'),
            89153: TrecQrel('https://github.com/christophehurpeau/SpringbokJS/blob/bc1069baafc0785d361a33ff5a2fa604b8b3b454/src/browser/base/S.History.js#L72-L78', 'https://github.com/christophehurpeau/SpringbokJS/blob/bc1069baafc0785d361a33ff5a2fa604b8b3b454/src/browser/base/S.History.js#L72-L78', 1, '0'),
        })
        self._test_qrels('codesearchnet/test', count=100529, items={
            0: TrecQrel('https://github.com/soimort/you-get/blob/b746ac01c9f39de94cac2d56f665285b0523b974/src/you_get/extractors/youtube.py#L135-L143', 'https://github.com/soimort/you-get/blob/b746ac01c9f39de94cac2d56f665285b0523b974/src/you_get/extractors/youtube.py#L135-L143', 1, '0'),
            9: TrecQrel('https://github.com/soimort/you-get/blob/b746ac01c9f39de94cac2d56f665285b0523b974/src/you_get/extractors/sina.py#L54-L64', 'https://github.com/soimort/you-get/blob/b746ac01c9f39de94cac2d56f665285b0523b974/src/you_get/extractors/sina.py#L54-L64', 1, '0'),
            100528: TrecQrel('https://github.com/dherges/grunt-bower-event/blob/ce7dc2303ef186ccf5eaa8d5b691102e13523076/tasks/lib/BowerTask.js#L24-L30', 'https://github.com/dherges/grunt-bower-event/blob/ce7dc2303ef186ccf5eaa8d5b691102e13523076/tasks/lib/BowerTask.js#L24-L30', 1, '0'),
        })
        self._test_qrels('codesearchnet/challenge', count=4006, items={
            0: CodeSearchNetChallengeQrel('71', 'https://github.com/tylertreat/BoomFilters/blob/611b3dbe80e85df3a0a10a43997d4d5784e86245/topk.go#L70-L85', '0', ''),
            9: CodeSearchNetChallengeQrel('24', 'https://github.com/uber-go/ratelimit/blob/c15da02342779cb6dc027fc95ee2277787698f36/internal/clock/clock.go#L66-L76', '1', ''),
            4005: CodeSearchNetChallengeQrel('45', 'https://github.com/conanite/aduki/blob/2e17522b9536fe0a12d2dd97ae601cabb2ee293e/lib/aduki.rb#L167-L176', '0', ''),
        })


if __name__ == '__main__':
    unittest.main()
