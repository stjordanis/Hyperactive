# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License


from ...base_optimizer import BaseOptimizer


class RandomAnnealingOptimizer(BaseOptimizer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        kwargs["eps"] = 100
        kwargs["t_rate"] = 0.98

        self.pos_para = {"eps": kwargs["eps"]}
        self.t_rate = kwargs["t_rate"]

        self.temp = 1

        self.initializer = self._init_rnd_annealing

    def _iterate(self, i, _cand_, _p_, X, y):
        _p_.pos_new = _p_.move_climb(_cand_, _p_.pos_current, eps_mod=self.temp)
        _p_.score_new = _cand_.eval_pos(_p_.pos_new, X, y)

        if _p_.score_new > _cand_.score_best:
            _cand_, _p_ = self._update_pos(_cand_, _p_)

        self.temp = self.temp * self.t_rate

        return _cand_

    def _init_rnd_annealing(self, _cand_, X, y):
        return super()._initialize(_cand_, pos_para=self.pos_para)
