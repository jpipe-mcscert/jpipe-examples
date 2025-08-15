######
## Justification final
######
import yaml

from typing import Any, Callable

from jpipe_runner.framework.decorators.jpipe_decorator import jpipe


RESOURCES_DIR = "resources/"

################
## Conclusion ##
################


## Conclusion c
@jpipe(consume=[])
def fairness_exists() -> bool:
    return True


###############
## Strategy  ##
###############


## Strategy training
@jpipe(consume=[], produce=[])
def training_model_using_the_multilingual_dataset(produce) -> bool:
    return True


## Strategy testing_multi_ling
@jpipe(consume=[], produce=[])
def evaluating_model_using_the_multilingual_benchmark(produce) -> bool:
    return True


## Strategy fairness_impl_methods
@jpipe(consume=[], produce=[])
def implementing_fairness_within_model(produce) -> bool:
    return True


## Strategy AND
@jpipe(consume=[], produce=[])
def and_(produce) -> bool:
    return True


## Strategy fairness_exe_methods
@jpipe(consume=[], produce=[])
def executing_fairness_benchmarks(produce) -> bool:
    return True


## Strategy testing_BBQ
@jpipe(consume=[], produce=[])
def evaluating_model_using_the_bbq_benchmark(produce) -> bool:
    return True


###############
## Evidence  ##
###############


## Evidence multi_ling_BM
@jpipe(consume=[], produce=[])
def multilingual_benchmark_is_present(produce) -> bool:
    return True


## Evidence training_code
@jpipe(consume=[], produce=[])
def training_code_is_present(produce) -> bool:
    return True


## Evidence BBQ_BM
@jpipe(consume=[], produce=[])
def bbq_benchmark_is_present(produce) -> bool:
    return True


## Evidence multi_ling_DS
@jpipe(consume=[], produce=["dataset_configuration"])
def multilingual_dataset_is_present(produce: Callable[[str, Any], None]) -> bool:
    EXPECTED_SMOLLM3_MODEL_NAME = "smollm3-3B-final"
    EXPECTED_PRETRAINING_LANGUAGES = [
        "fw2-fra",
        "fw2-spa",
        "fw2-deu",
        "fw2-ita",
        "fw2-por",
        "fw2-cmn",
        "fw2-rus",
        "fw2-fas",
        "fw2-jpn",
        "fw2-kor",
        "fw2-hin",
        "fw2-tha",
        "fw2-vie",
        "fw2-ell",
    ]

    with open(f"{RESOURCES_DIR}/pretraining/stage1_8T.yaml") as f:
        try:
            pretraining_stage1_run_configuration = yaml.safe_load(f)
            # comparing the model name to be sure it is smollm3
            assert (
                pretraining_stage1_run_configuration["general"]["project"]
                == EXPECTED_SMOLLM3_MODEL_NAME
            )
            # comparing the listed datasets with the expected supported languages
            dataset_configuration = pretraining_stage1_run_configuration["data_stages"][
                0
            ]["data"]["dataset"]
            all_pretraining_datasets = dataset_configuration["dataset_read_path"]
            for pretraining_language in EXPECTED_PRETRAINING_LANGUAGES:
                assert (
                    f"/scratch/smollm3-data-part1/{pretraining_language}"
                    in all_pretraining_datasets
                ), f"missing language [{pretraining_language}] in pretraining datasets"
            produce("dataset_configuration", dataset_configuration)
            return True
        except (yaml.YAMLError, AssertionError) as exc:
            print(exc)
            return False


## Evidence evaluated_code
@jpipe(consume=[], produce=[])
def evaluation_code_is_present(produce) -> bool:
    return True
