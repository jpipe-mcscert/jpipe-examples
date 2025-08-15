######
## Justification final
######
import httpx
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
@jpipe(consume=["dataset_configuration", "training_code"], produce=[])
def training_model_using_the_multilingual_dataset(
    produce: Callable[[str, Any], None],
) -> bool:
    return True


## Strategy testing_multi_ling
@jpipe(consume=["eval_configuration", "evaluation_procedure"], produce=[])
def evaluating_model_using_the_multilingual_benchmark(
    produce: Callable[[str, Any], None],
) -> bool:
    return True


## Strategy fairness_impl_methods
@jpipe(consume=[], produce=[])
def implementing_fairness_within_model(produce: Callable[[str, Any], None]) -> bool:
    return True


## Strategy AND
@jpipe(consume=[], produce=[])
def and_(produce) -> bool:
    return True


## Strategy fairness_exe_methods
@jpipe(consume=[], produce=[])
def executing_fairness_benchmarks(produce: Callable[[str, Any], None]) -> bool:
    return True


## Strategy testing_BBQ
@jpipe(consume=["evaluation_procedure", "bbq_benchmark"], produce=[])
def evaluating_model_using_the_bbq_benchmark(
    produce: Callable[[str, Any], None],
) -> bool:
    return True


###############
## Evidence  ##
###############


## Evidence multi_ling_BM
@jpipe(consume=[], produce=["eval_configuration"])
def multilingual_benchmark_is_present(produce: Callable[[str, Any], None]) -> bool:
    EXPECTED_PRETRAINING_BENCHMARKS_ = [
        # MLMM Hellaswag
        "mlmm_hellaswag_ara_cf",
        "mlmm_hellaswag_rus_cf",
        "mlmm_hellaswag_zho_cf",
        "mlmm_hellaswag_deu_cf",
        "mlmm_hellaswag_fra_cf",
        "mlmm_hellaswag_ita_cf",
        "mlmm_hellaswag_por_cf",
        "mlmm_hellaswag_spa_cf",
        # Belebele
        "belebele_arb_Arab_cf",
        "belebele_rus_Cyrl_cf",
        "belebele_zho_Hans_cf",
        "belebele_deu_Latn_cf",
        "belebele_fra_Latn_cf",
        "belebele_ita_Latn_cf",
        "belebele_por_Latn_cf",
        "belebele_spa_Latn_cf",
        "belebele_eng_Latn_cf",
        # Global MMLU (CF)
        "global_mmlu_ca_ara_cf",
        "global_mmlu_ca_rus_cf",
        "global_mmlu_ca_zho_cf",
        "global_mmlu_ca_deu_cf",
        "global_mmlu_ca_fra_cf",
        "global_mmlu_ca_ita_cf",
        "global_mmlu_ca_por_cf",
        "global_mmlu_ca_spa_cf",
        # Flores200
        "flores200:fra_Latn-eng_Latn",
        "flores200:eng_Latn-fra_Latn",
        "flores200:spa_Latn-eng_Latn",
        "flores200:eng_Latn-spa_Latn",
        "flores200:deu_Latn-eng_Latn",
        "flores200:eng_Latn-deu_Latn",
        "flores200:ita_Latn-eng_Latn",
        "flores200:eng_Latn-ita_Latn",
        "flores200:por_Latn-eng_Latn",
        "flores200:eng_Latn-por_Latn",
        "flores200:zho_Hans-eng_Latn",
        "flores200:eng_Latn-zho_Hans",
        "flores200:rus_Cyrl-eng_Latn",
        "flores200:eng_Latn-rus_Cyrl",
        "flores200:arb_Arab-eng_Latn",
        "flores200:eng_Latn-arb_Arab",
    ]

    with open(f"{RESOURCES_DIR}/eval/smollm3_base.txt") as f:
        eval_configuration = f.read()
        # comparing the listed benchmarks with the expected supported languages
        remaining = [
            e
            for e in EXPECTED_PRETRAINING_BENCHMARKS_
            if f"lighteval|{e}" not in eval_configuration
        ]
        assert not remaining, f"missing language benchmark(s) {remaining} in eval"

        produce("eval_configuration", eval_configuration)
    return True


## Evidence training_code
@jpipe(consume=[], produce=["training_code"])
def training_code_is_present(produce: Callable[[str, Any], None]) -> bool:
    EXPECTED_TRAIN_SCRIPT_LOCATION = "https://raw.githubusercontent.com/huggingface/nanotron/refs/heads/main/run_train.py"

    training_code_query = httpx.get(EXPECTED_TRAIN_SCRIPT_LOCATION)
    training_code_query.raise_for_status()

    produce("training_code", training_code_query.text)

    return True


## Evidence BBQ_BM
@jpipe(consume=[], produce=["bbq_benchmark"])
def bbq_benchmark_is_present(produce: Callable[[str, Any], None]) -> bool:
    produce("bbq_benchmark", "TODO")
    return False


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
        pretraining_stage1_run_configuration = yaml.safe_load(f)
        # comparing the model name to be sure it is smollm3
        assert (
            pretraining_stage1_run_configuration["general"]["project"]
            == EXPECTED_SMOLLM3_MODEL_NAME
        )
        # comparing the listed datasets with the expected supported languages
        dataset_configuration = pretraining_stage1_run_configuration["data_stages"][0][
            "data"
        ]["dataset"]
        all_pretraining_datasets = dataset_configuration["dataset_read_path"]
        for pretraining_language in EXPECTED_PRETRAINING_LANGUAGES:
            assert (
                f"/scratch/smollm3-data-part1/{pretraining_language}"
                in all_pretraining_datasets
            ), f"missing language [{pretraining_language}] in pretraining datasets"
        produce("dataset_configuration", dataset_configuration)
    return True


## Evidence evaluated_code
@jpipe(consume=[], produce=["evaluation_procedure"])
def evaluation_code_is_present(produce: Callable[[str, Any], None]) -> bool:
    EXPECTED_EVALUATION_README_LOCATION = "https://raw.githubusercontent.com/huggingface/smollm/refs/heads/main/text/evaluation/smollm3/README.md"

    evaluation_readme_query = httpx.get(EXPECTED_EVALUATION_README_LOCATION)
    evaluation_readme_query.raise_for_status()

    produce("evaluation_procedure", evaluation_readme_query.text)

    return True
