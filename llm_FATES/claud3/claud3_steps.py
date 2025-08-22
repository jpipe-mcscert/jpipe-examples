import httpx
from jpipe_runner.framework.decorators.jpipe_decorator import jpipe


######
## Justification final
######

## Strategy all_risks
def aggregating_all_catastrophic_risks_and_severe_harms_metrics() -> bool:
    return True


## Evidence quality
@jpipe(consume=["quality_benchmark_link"], produce=["quality_benchmark_is_present"])
def quality_benchmark_is_present(quality_benchmark_link: str, produce) -> bool:
    """
    Check if the quality benchmark is present by pinging the link.
    :param quality_benchmark_link: The URL of the quality benchmark to check.
    :param produce: A function to produce the result of the check.
    :return: True if the benchmark is present, otherwise False.
    """
    httpx.get(quality_benchmark_link).raise_for_status()
    produce("quality_benchmark_is_present", True)
    return True


## Evidence model
@jpipe(consume=["model_link"], produce=["model_is_present"])
def model_is_trained_and_available(model_link: str, produce) -> bool:
    """
    Check if the model is trained and available by pinging the model link.
    :param model_link: The URL of the model to check.
    :param produce: A function to produce the result of the check.
    :return: True if the model is available, otherwise False.
    """
    httpx.get(model_link).raise_for_status()
    produce("benchmark_is_present", True)
    return True


## Evidence NIAH
@jpipe(consume=["niah_benchmark_link"], produce=["niah_benchmark_is_present"])
def needle_in_a_haystack_benchmark_is_present(niah_benchmark_link: str, produce) -> bool:
    """
    Ping the link
    :param niah_benchmark_link: The URL of the benchmark to check.
    :param produce: A function to produce the result of the check.
    :return: True if the benchmark is present, otherwise False.
    """
    httpx.get(niah_benchmark_link).raise_for_status()
    produce("niah_benchmark_is_present", True)
    return True


## Strategy long_context_strat
@jpipe(consume=[
    "niah_benchmark_is_present",
    "niah_threshold",
    "niah_benchmark_result",
    "model_is_present",
    "quality_benchmark_is_present",
    "quality_threshold",
    "quality_benchmark_result"
])
def evaluating_the_long_context_performance_of_the_model(model_is_present: bool,
                                                         niah_benchmark_is_present: bool,
                                                         niah_threshold: float,
                                                         niah_benchmark_result: float,
                                                         quality_benchmark_is_present: bool,
                                                         quality_threshold: float,
                                                         quality_benchmark_result: float
                                                         ) -> bool:
    """
    Evaluating the long context performance of the model based on benchmark results.
    :param model_is_present: true if the model is available, false otherwise.
    :param niah_benchmark_is_present: true if the benchmark is present, false otherwise.
    :param niah_threshold: the threshold value to compare against the benchmark result.
    :param niah_benchmark_result: the result of the benchmark evaluation.
    :param quality_benchmark_is_present: true if the quality benchmark is present, false otherwise.
    :param quality_threshold: the threshold value for the quality benchmark.
    :param quality_benchmark_result: the result of the quality benchmark evaluation.
    :return: True if the benchmark is present and the result meets or exceeds the threshold, otherwise False.
    """
    if (
            not niah_benchmark_is_present or
            not model_is_present or
            not quality_benchmark_is_present
    ):
        return False
    return niah_benchmark_result >= niah_threshold and \
        quality_benchmark_result >= quality_threshold


## Strategy bias_strat
def assessing_bias() -> bool:
    return True


## Strategy safety_strat
def checking_if_safety_strat_are_available() -> bool:
    return True


## Strategy chemical_strat
def assessing_chemical_risk_level() -> bool:
    return True


## Evidence ctf
def capture_the_flag_challenges_are_available() -> bool:
    return True


## Strategy all_safety
def aggregating_all_prevention_misuse_measures_and_enforcement_of_safe_behavior() -> bool:
    return True


## Strategy fact_acc_strat
def evaluating_the_factual_accuracy_of_the_model() -> bool:
    return True


## Evidence discrimination_ds
def discrimination_dataset_exist() -> bool:
    return True


## Strategy cyber_strat
def assessing_cyber_capabilities() -> bool:
    return True


## Strategy ara_strat
def evaluating_ara_capabilities_of_the_models() -> bool:
    return True


## Conclusion c
def this_model_is_safe_and_secure() -> bool:
    return True


## Strategy disc_strat
def assessing_discrimination_over_different_demographic_groups() -> bool:
    return True


## Strategy biological_strat
def assessing_biological_risks_level() -> bool:
    return True


## Evidence red_teaming
def red_teaming_is_available() -> bool:
    return True


## Evidence ara_list
def list_of_ara_tasks_is_available() -> bool:
    return True


## Evidence multi_factual
def multi_factual_benchmark_is_present() -> bool:
    return True


## Evidence control
def control_group_with_access_to_google_is_available() -> bool:
    return True


## Evidence oneHundredQ_hard
def onehundredq_hard_benchmark_is_present() -> bool:
    return True


## Strategy all_social_risks
def aggregating_all_social_metrics() -> bool:
    return True


## Evidence safety_policy
def safety_policies_measures_exists() -> bool:
    return True


## Strategy strat
def ensuring_that_the_model_provide_factual_information() -> bool:
    return True


## Evidence bbq
def bbq_benchmark_exist() -> bool:
    return True


## Strategy cbrn_strat
def assessing_cbrn_risks_levels() -> bool:
    return True


## Evidence easymedium_QA
def easy_medium_qa_benchmark_is_present() -> bool:
    return True


## Strategy AND
def combining_safety_and_security_implementations_evaluations() -> bool:
    return True


## Strategy discovery_exploit
def evaluating_vulnerability_discovery_and_exploit_development_capabilities() -> bool:
    return True


## Evidence experts
def specifc_experts_are_available() -> bool:
    return True
