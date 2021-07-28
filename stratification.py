def __weightedAverage(measure, data):
    data_points = [d for d in data if
                   d[measure["weightingField"]] is not None and d[measure["weightedField"]] is not None]
    numerator = sum(d[measure["weightingField"]] * d[measure["weightedField"]] for d in data_points)
    denominator = sum(d[measure["weightingField"]] for d in data_points)
    return numerator / denominator if denominator != 0 else None


__stratification_measure_computations = {"count": lambda _, data: len(data),
                                         "sum": lambda measure, data: sum(d[measure["field"]] for d in data),
                                         "weightedAverage": __weightedAverage}


def __format_range(value_formatter, bucket, step):
    if "label" in bucket:
        return bucket["label"]
    if "min" in bucket and "max" in bucket:
        return f"{value_formatter(bucket['min'])} - {value_formatter(bucket['max'] - step)}"
    if "min" in bucket:
        return f">= {value_formatter(bucket['min'])}"
    if "max" in bucket:
        return f"< {value_formatter(bucket['max'])}"
    return "None"


label_formatters = {
    "percent": lambda label_def, bucket, step: __format_range(
        lambda value: str(round(value * 100, label_def["scale"])) + ("%" if label_def["symbol"] else ""), bucket, step),
    "number": lambda label_def, bucket, step: __format_range(
        lambda value: '{:,}'.format(round(value, label_def["scale"])) if label_def["separator"] else round(value,
                                                                                                           label_def[
                                                                                                               "scale"]),
        bucket, step
    )
}


def stratify(data, stratification_definition, stratification_measures):
    buckets = [{**b,
        "name": label_formatters[stratification_definition["label"]["format"]](
            stratification_definition["label"], b,
            stratification_definition["step"]),
        "values": []}
        for b in
        stratification_definition["buckets"]]

    for datum in data:
        matched_buckets = [b for b in buckets if
                           b["field"] in datum and datum[b["field"]] is not None and (
                                       "exactly" not in b and ("min" not in b or (
                                       datum[b["field"]] > b["min"])) and (
                                               "max" not in b or (
                                               b["field"] in datum and datum[b["field"]] <= b["max"]))) or (
                                       "exactly" in b and datum[b["field"]] == b["exactly"])]
        if len(matched_buckets) > 0:
            matched_buckets[0]["values"].append(datum)

    return [
        {**{"name": b["name"]}, **{m["name"]: __stratification_measure_computations[m["type"]](m, b["values"]) for m in
                                   stratification_measures}} for b in buckets]
