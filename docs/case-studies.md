---
title: Case Studies of Python Assertions in ML Jupyter Notebooks
---

# Shape checking

## HOLD decile-9.2

```python
assert len(nb_states) == len(nb_actions), 'Given array must have the same size'
```

Description: The assertion checks that the shape of two lists is the same.

I don't see a clear link with what we are trying to do here. Also, there are no markdown cells that describe what is going on in the code.

## SELECT decile-8.2

```python
assert dB2.shape == B2.shape
```

Description: The assertion checks that the shape of two given matrices is the same.

The notebook presents a tutorial on implementing a Neural Network from scratch. The assertion is defined within the `gradient` method which accepts the weights and biases as parameter and calculates their gradient. The assertion ensures that the same of the gradient `dB2` is the same as the bias `B2`.

The shapes must match since the new weights and biases are calculated by multiplying the prior weights and biases with their gradiants (see `updates` method definition for more info). The question is, when can this assertion fail? In other words, when can the shape of the gradient change?

# Existance checking

## HOLD decile-7.2

```python
assert self.teacher_model is not None, 'target encoder has not been created yet'
```

Description: The assertion ensures that `teacher_model` exists.

The notebook is something to do with the CIFAR10 dataset, but there is not enough context for me to understand whats going on here.