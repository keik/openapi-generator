# coding: utf-8

"""
    openapi 3.0.3 sample spec

    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""

import unittest

import unit_test_api
from unit_test_api.model.uniqueitems_false_validation import UniqueitemsFalseValidation
from unit_test_api import configuration


class TestUniqueitemsFalseValidation(unittest.TestCase):
    """UniqueitemsFalseValidation unit test stubs"""
    _configuration = configuration.Configuration()

    def test_non_unique_array_of_integers_is_valid_passes(self):
        # non-unique array of integers is valid
        UniqueitemsFalseValidation._from_openapi_data(
            [
                1,
                1,
            ],
            _configuration=self._configuration
        )

    def test_unique_array_of_objects_is_valid_passes(self):
        # unique array of objects is valid
        UniqueitemsFalseValidation._from_openapi_data(
            [
                {
                    "foo":
                        "bar",
                },
                {
                    "foo":
                        "baz",
                },
            ],
            _configuration=self._configuration
        )

    def test_non_unique_array_of_nested_objects_is_valid_passes(self):
        # non-unique array of nested objects is valid
        UniqueitemsFalseValidation._from_openapi_data(
            [
                {
                    "foo":
                        {
                            "bar":
                                {
                                    "baz":
                                        True,
                                },
                        },
                },
                {
                    "foo":
                        {
                            "bar":
                                {
                                    "baz":
                                        True,
                                },
                        },
                },
            ],
            _configuration=self._configuration
        )

    def test_non_unique_array_of_objects_is_valid_passes(self):
        # non-unique array of objects is valid
        UniqueitemsFalseValidation._from_openapi_data(
            [
                {
                    "foo":
                        "bar",
                },
                {
                    "foo":
                        "bar",
                },
            ],
            _configuration=self._configuration
        )

    def test_1_and_true_are_unique_passes(self):
        # 1 and true are unique
        UniqueitemsFalseValidation._from_openapi_data(
            [
                1,
                True,
            ],
            _configuration=self._configuration
        )

    def test_unique_array_of_integers_is_valid_passes(self):
        # unique array of integers is valid
        UniqueitemsFalseValidation._from_openapi_data(
            [
                1,
                2,
            ],
            _configuration=self._configuration
        )

    def test_non_unique_array_of_arrays_is_valid_passes(self):
        # non-unique array of arrays is valid
        UniqueitemsFalseValidation._from_openapi_data(
            [
                [
                    "foo",
                ],
                [
                    "foo",
                ],
            ],
            _configuration=self._configuration
        )

    def test_numbers_are_unique_if_mathematically_unequal_passes(self):
        # numbers are unique if mathematically unequal
        UniqueitemsFalseValidation._from_openapi_data(
            [
                1.0,
                1.0,
                1,
            ],
            _configuration=self._configuration
        )

    def test_false_is_not_equal_to_zero_passes(self):
        # false is not equal to zero
        UniqueitemsFalseValidation._from_openapi_data(
            [
                0,
                False,
            ],
            _configuration=self._configuration
        )

    def test_unique_array_of_nested_objects_is_valid_passes(self):
        # unique array of nested objects is valid
        UniqueitemsFalseValidation._from_openapi_data(
            [
                {
                    "foo":
                        {
                            "bar":
                                {
                                    "baz":
                                        True,
                                },
                        },
                },
                {
                    "foo":
                        {
                            "bar":
                                {
                                    "baz":
                                        False,
                                },
                        },
                },
            ],
            _configuration=self._configuration
        )

    def test_0_and_false_are_unique_passes(self):
        # 0 and false are unique
        UniqueitemsFalseValidation._from_openapi_data(
            [
                0,
                False,
            ],
            _configuration=self._configuration
        )

    def test_unique_array_of_arrays_is_valid_passes(self):
        # unique array of arrays is valid
        UniqueitemsFalseValidation._from_openapi_data(
            [
                [
                    "foo",
                ],
                [
                    "bar",
                ],
            ],
            _configuration=self._configuration
        )

    def test_true_is_not_equal_to_one_passes(self):
        # true is not equal to one
        UniqueitemsFalseValidation._from_openapi_data(
            [
                1,
                True,
            ],
            _configuration=self._configuration
        )

    def test_non_unique_heterogeneous_types_are_valid_passes(self):
        # non-unique heterogeneous types are valid
        UniqueitemsFalseValidation._from_openapi_data(
            [
                {
                },
                [
                    1,
                ],
                True,
                None,
                {
                },
                1,
            ],
            _configuration=self._configuration
        )

    def test_unique_heterogeneous_types_are_valid_passes(self):
        # unique heterogeneous types are valid
        UniqueitemsFalseValidation._from_openapi_data(
            [
                {
                },
                [
                    1,
                ],
                True,
                None,
                1,
            ],
            _configuration=self._configuration
        )


if __name__ == '__main__':
    unittest.main()
