# -- FILE: features/steps/test_steps.py
from behave import given, when, then, step
import subprocess


@given('range of integer numbers from {number_from:d} to {number_to:d}')
def step_impl(context, number_from, number_to):
    context.num_from = number_from
    context.num_to = number_to


@when('executing the {script_name} script with numbers from the given range one by one as its argument to check results')
def step_impl(context, script_name):
    context.fizz_count = 0
    context.buzz_count = 0
    context.fizzbuzz_count = 0
    context.other_count = 0
    for n in range(context.num_from, context.num_to):
        p = subprocess.Popen("python " + script_name + " " + str(n), stdout=subprocess.PIPE, shell=True)
        out, err = p.communicate()
        if n % 3 == 0 and n % 5 != 0:
            assert "fizz" in str(out) and "buzz" not in str(out)
            context.fizz_count += 1
        if n % 3 != 0 and n % 5 == 0:
            assert "fizz" not in str(out) and "buzz" in str(out)
            context.buzz_count += 1
        if n % 3 == 0 and n % 5 == 0:
            assert "fizz" in str(out) and "buzz" in str(out)
            context.fizzbuzz_count += 1
        if n % 3 != 0 and n % 5 != 0:
            assert str(n) in str(out)
            context.other_count += 1


@then('check if all result types are present')
def step_impl(context):
    assert context.fizz_count > 0
    assert context.buzz_count > 0
    assert context.fizzbuzz_count > 0
    assert context.other_count > 0
