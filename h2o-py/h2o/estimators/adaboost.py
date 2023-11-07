#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# This file is auto-generated by h2o-3/h2o-bindings/bin/gen_python.py
# Copyright 2016 H2O.ai;  Apache License Version 2.0 (see LICENSE for details)
#

from h2o.estimators.estimator_base import H2OEstimator
from h2o.exceptions import H2OValueError
from h2o.frame import H2OFrame
from h2o.utils.typechecks import assert_is_type, Enum, numeric


class H2OAdaBoostEstimator(H2OEstimator):
    """
    AdaBoost

    Builds an AdaBoost model
    """

    algo = "adaboost"
    supervised_learning = True

    def __init__(self,
                 model_id=None,  # type: Optional[Union[None, str, H2OEstimator]]
                 training_frame=None,  # type: Optional[Union[None, str, H2OFrame]]
                 ignored_columns=None,  # type: Optional[List[str]]
                 ignore_const_cols=True,  # type: bool
                 categorical_encoding="auto",  # type: Literal["auto", "enum", "one_hot_internal", "one_hot_explicit", "binary", "eigen", "label_encoder", "sort_by_response", "enum_limited"]
                 weights_column=None,  # type: Optional[str]
                 nlearners=50,  # type: int
                 weak_learner="auto",  # type: Literal["auto", "drf", "glm", "gbm"]
                 learn_rate=0.5,  # type: float
                 seed=-1,  # type: int
                 ):
        """
        :param model_id: Destination id for this model; auto-generated if not specified.
               Defaults to ``None``.
        :type model_id: Union[None, str, H2OEstimator], optional
        :param training_frame: Id of the training data frame.
               Defaults to ``None``.
        :type training_frame: Union[None, str, H2OFrame], optional
        :param ignored_columns: Names of columns to ignore for training.
               Defaults to ``None``.
        :type ignored_columns: List[str], optional
        :param ignore_const_cols: Ignore constant columns.
               Defaults to ``True``.
        :type ignore_const_cols: bool
        :param categorical_encoding: Encoding scheme for categorical features
               Defaults to ``"auto"``.
        :type categorical_encoding: Literal["auto", "enum", "one_hot_internal", "one_hot_explicit", "binary", "eigen", "label_encoder",
               "sort_by_response", "enum_limited"]
        :param weights_column: Column with observation weights. Giving some observation a weight of zero is equivalent
               to excluding it from the dataset; giving an observation a relative weight of 2 is equivalent to repeating
               that row twice. Negative weights are not allowed. Note: Weights are per-row observation weights and do
               not increase the size of the data frame. This is typically the number of times a row is repeated, but
               non-integer values are supported as well. During training, rows with higher weights matter more, due to
               the larger loss function pre-factor. If you set weight = 0 for a row, the returned prediction frame at
               that row is zero and this is incorrect. To get an accurate prediction, remove all rows with weight == 0.
               Defaults to ``None``.
        :type weights_column: str, optional
        :param nlearners: Number of AdaBoost weak learners.
               Defaults to ``50``.
        :type nlearners: int
        :param weak_learner: Choose a weak learner type. Defaults to AUTO, which means DRF.
               Defaults to ``"auto"``.
        :type weak_learner: Literal["auto", "drf", "glm", "gbm"]
        :param learn_rate: Learning rate (from 0.0 to 1.0)
               Defaults to ``0.5``.
        :type learn_rate: float
        :param seed: Seed for pseudo random number generator (if applicable)
               Defaults to ``-1``.
        :type seed: int
        """
        super(H2OAdaBoostEstimator, self).__init__()
        self._parms = {}
        self._id = self._parms['model_id'] = model_id
        self.training_frame = training_frame
        self.ignored_columns = ignored_columns
        self.ignore_const_cols = ignore_const_cols
        self.categorical_encoding = categorical_encoding
        self.weights_column = weights_column
        self.nlearners = nlearners
        self.weak_learner = weak_learner
        self.learn_rate = learn_rate
        self.seed = seed

    @property
    def training_frame(self):
        """
        Id of the training data frame.

        Type: ``Union[None, str, H2OFrame]``.
        """
        return self._parms.get("training_frame")

    @training_frame.setter
    def training_frame(self, training_frame):
        self._parms["training_frame"] = H2OFrame._validate(training_frame, 'training_frame')

    @property
    def ignored_columns(self):
        """
        Names of columns to ignore for training.

        Type: ``List[str]``.
        """
        return self._parms.get("ignored_columns")

    @ignored_columns.setter
    def ignored_columns(self, ignored_columns):
        assert_is_type(ignored_columns, None, [str])
        self._parms["ignored_columns"] = ignored_columns

    @property
    def ignore_const_cols(self):
        """
        Ignore constant columns.

        Type: ``bool``, defaults to ``True``.
        """
        return self._parms.get("ignore_const_cols")

    @ignore_const_cols.setter
    def ignore_const_cols(self, ignore_const_cols):
        assert_is_type(ignore_const_cols, None, bool)
        self._parms["ignore_const_cols"] = ignore_const_cols

    @property
    def categorical_encoding(self):
        """
        Encoding scheme for categorical features

        Type: ``Literal["auto", "enum", "one_hot_internal", "one_hot_explicit", "binary", "eigen", "label_encoder",
        "sort_by_response", "enum_limited"]``, defaults to ``"auto"``.
        """
        return self._parms.get("categorical_encoding")

    @categorical_encoding.setter
    def categorical_encoding(self, categorical_encoding):
        assert_is_type(categorical_encoding, None, Enum("auto", "enum", "one_hot_internal", "one_hot_explicit", "binary", "eigen", "label_encoder", "sort_by_response", "enum_limited"))
        self._parms["categorical_encoding"] = categorical_encoding

    @property
    def weights_column(self):
        """
        Column with observation weights. Giving some observation a weight of zero is equivalent to excluding it from the
        dataset; giving an observation a relative weight of 2 is equivalent to repeating that row twice. Negative
        weights are not allowed. Note: Weights are per-row observation weights and do not increase the size of the data
        frame. This is typically the number of times a row is repeated, but non-integer values are supported as well.
        During training, rows with higher weights matter more, due to the larger loss function pre-factor. If you set
        weight = 0 for a row, the returned prediction frame at that row is zero and this is incorrect. To get an
        accurate prediction, remove all rows with weight == 0.

        Type: ``str``.
        """
        return self._parms.get("weights_column")

    @weights_column.setter
    def weights_column(self, weights_column):
        assert_is_type(weights_column, None, str)
        self._parms["weights_column"] = weights_column

    @property
    def nlearners(self):
        """
        Number of AdaBoost weak learners.

        Type: ``int``, defaults to ``50``.
        """
        return self._parms.get("nlearners")

    @nlearners.setter
    def nlearners(self, nlearners):
        assert_is_type(nlearners, None, int)
        self._parms["nlearners"] = nlearners

    @property
    def weak_learner(self):
        """
        Choose a weak learner type. Defaults to AUTO, which means DRF.

        Type: ``Literal["auto", "drf", "glm", "gbm"]``, defaults to ``"auto"``.
        """
        return self._parms.get("weak_learner")

    @weak_learner.setter
    def weak_learner(self, weak_learner):
        assert_is_type(weak_learner, None, Enum("auto", "drf", "glm", "gbm"))
        self._parms["weak_learner"] = weak_learner

    @property
    def learn_rate(self):
        """
        Learning rate (from 0.0 to 1.0)

        Type: ``float``, defaults to ``0.5``.
        """
        return self._parms.get("learn_rate")

    @learn_rate.setter
    def learn_rate(self, learn_rate):
        assert_is_type(learn_rate, None, numeric)
        self._parms["learn_rate"] = learn_rate

    @property
    def seed(self):
        """
        Seed for pseudo random number generator (if applicable)

        Type: ``int``, defaults to ``-1``.
        """
        return self._parms.get("seed")

    @seed.setter
    def seed(self, seed):
        assert_is_type(seed, None, int)
        self._parms["seed"] = seed

