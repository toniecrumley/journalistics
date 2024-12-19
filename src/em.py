import random

samples = []
samples.append({
    "flips": "HTTHTTTHTT",
    "likelihood_a": 0.0,
    "likelihood_b": 0.0,
    "probability_a": 0.0,
    "probability_b": 0.0,
    "coin_a_heads": 0.0,
    "coin_a_tails": 0.0,
    "coin_b_heads": 0.0,
    "coin_b_tails": 0.0
})
samples.append({
    "flips": "THTTHTTTHH",
    "likelihood_a": 0.0,
    "likelihood_b": 0.0,
    "probability_a": 0.0,
    "probability_b": 0.0,
    "coin_a_heads": 0.0,
    "coin_a_tails": 0.0,
    "coin_b_heads": 0.0,
    "coin_b_tails": 0.0
})
samples.append({
    "flips": "HHTHHTHTHH",
    "likelihood_a": 0.0,
    "likelihood_b": 0.0,
    "probability_a": 0.0,
    "probability_b": 0.0,
    "coin_a_heads": 0.0,
    "coin_a_tails": 0.0,
    "coin_b_heads": 0.0,
    "coin_b_tails": 0.0
})
samples.append({
    "flips": "HHHTHHHHHH",
    "likelihood_a": 0.0,
    "likelihood_b": 0.0,
    "probability_a": 0.0,
    "probability_b": 0.0,
    "coin_a_heads": 0.0,
    "coin_a_tails": 0.0,
    "coin_b_heads": 0.0,
    "coin_b_tails": 0.0
})

theta_a = random.random()
theta_b = 1.0 - theta_a
theta_a = 0.5
theta_b = 0.5
print(theta_a, theta_b)

for _ in range(10):
    for sample in samples:
        heads_count = sample["flips"].count("H")
        tails_count = sample["flips"].count("T")
        sample["likelihood_a"] = theta_a**heads_count * (1 - theta_a)**tails_count
        sample["likelihood_b"] = theta_b**heads_count * (1 - theta_b)**tails_count

        total_likelihood = sample["likelihood_a"] + sample["likelihood_b"]
        sample["probability_a"] = sample["likelihood_a"] / total_likelihood
        sample["probability_b"] = sample["likelihood_b"] / total_likelihood

        sample["coin_a_heads"] = sample["probability_a"] * heads_count
        sample["coin_a_tails"] = sample["probability_a"] * tails_count

        sample["coin_b_heads"] = sample["probability_b"] * heads_count
        sample["coin_b_tails"] = sample["probability_b"] * tails_count

    total_heads = 0.0
    total_tails = 0.0
    for sample in samples:
        total_heads += sample["coin_a_heads"]
        total_tails += sample["coin_a_tails"]
    theta_a = total_heads / (total_heads + total_tails)

    total_heads = 0.0
    total_tails = 0.0
    for sample in samples:
        total_heads += sample["coin_b_heads"]
        total_tails += sample["coin_b_tails"]
    theta_b = total_heads / (total_heads + total_tails)

    print(theta_a, theta_b)
