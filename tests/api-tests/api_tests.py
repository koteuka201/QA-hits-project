import requests
from lib.api_helper import get_page, post_form
import pytest

class TestHttpBaseChecks:

    def test_http_ok_on_root_page(self):
        assert get_page().status_code == 200

    def test_http_text_non_empty(self):
        assert get_page().text

    def test_http_ok_results_page(self):
        assert post_form(data = {
            'numCourses': 2,
            'prerequisites': '1,0'
        }).status_code == 200

    def test_form_content_type_text_hmtl(self):
        assert get_page().headers['Content-Type'] == 'text/html; charset=utf-8'

    def test_form_content_type_app_json(self):
        assert post_form(data = {
            'numCourses': 2,
            'prerequisites': '1,0'
        }).headers['Content-Type'] == 'application/json'

class TestCanFinish:

    def test_can_finish(self):
        data = {
            'numCourses': 2,
            'prerequisites': '1,0'
        }
        assert post_form(data = data).json()['result']

    @pytest.mark.parametrize("numCourses, prerequisites",[
        pytest.param(1,[], id="left_on_bound"),
        pytest.param(2, [[1,0]], id="left_gt_bound"),
        pytest.param(1999, [[1,0]], id="right_on_bound"),
        pytest.param(2000, [[1,0]], id="right_lt_bound")
    ])
    def test_can_finish_numCourses_count_valid(self, numCourses, prerequisites):

        assert post_form(data = {
            'numCourses': numCourses,
            'prerequisites': ';'.join([','.join(map(str, pair)) for pair in prerequisites])

        }).json()['result']


    @pytest.mark.parametrize("numCourses, prerequisites", [
        pytest.param(0, [], id="left_lt_bound"),
        pytest.param(2001, [[1, 0]], id="right_gt_bound")
    ])
    def test_bad_request_can_finish_numCourses_count_invalid(self, numCourses, prerequisites):
        assert post_form(data = {
            'numCourses': numCourses,
            'prerequisites': ';'.join([','.join(map(str, pair)) for pair in prerequisites])
        }).status_code == 400

    @pytest.mark.parametrize("numCourses, prerequisites", [
        pytest.param(1, [], id="left_on_bound"),
        pytest.param(2, [[1, 0]], id="left_gt_bound"),
        # pytest.param(1000, [[i % 4999, (i - 1) % 4999] for i in range(1, 4999)], id="right_on_bound"),
        # pytest.param(1000, [[i % 5000, (i - 1) % 5000] for i in range(1, 5000)], id="right_lt_bound")
    ])
    def test_can_finish_prerequisites_length_valid(self, numCourses, prerequisites):

        assert post_form(data = {
            'numCourses': numCourses,
            'prerequisites': ';'.join([','.join(map(str, pair)) for pair in prerequisites])

        }).json()['result']

    @pytest.mark.parametrize("numCourses, prerequisites", [
        pytest.param(1000, [[i % 5001, (i - 1) % 5001] for i in range(1, 5001)], id="right_gt_bound")
    ])
    def test_bad_request_can_finish_prerequisites_length_invalid(self, numCourses, prerequisites):
        assert post_form(data={
            'numCourses': numCourses,
            'prerequisites': ';'.join([','.join(map(str, pair)) for pair in prerequisites])
        }).status_code == 400

    @pytest.mark.parametrize("numCourses, prerequisites", [
        pytest.param(2, [[1,0]]),
        pytest.param(5, [[4, 0]]),
    ])
    def test_can_finish_prerequisites_i_ai_bi_valid(self, numCourses, prerequisites):
        assert post_form(data={
            'numCourses': numCourses,
            'prerequisites': ';'.join([','.join(map(str, pair)) for pair in prerequisites])
        }).json()['result']

    @pytest.mark.parametrize("numCourses, prerequisites", [
        pytest.param(2,[[-1,0]]),
        pytest.param(2,[[2,0]]),
        pytest.param(2,[[3,0]]),
    ])
    def test_bad_request_can_finish_prerequisites_i_ai_bi_invalid(self, numCourses, prerequisites):
        assert post_form(data={
            'numCourses': numCourses,
            'prerequisites': ';'.join([','.join(map(str, pair)) for pair in prerequisites])
        }).status_code == 400


    @pytest.mark.parametrize("numCourses, prerequisites", [
        pytest.param(3, [[1,0],[2,0]]),
    ])
    def test_can_finish_all_pairs_prerequisites_i_unique(self, numCourses, prerequisites):
        assert post_form(data={
            'numCourses': numCourses,
            'prerequisites': ';'.join([','.join(map(str, pair)) for pair in prerequisites])

        }).json()['result']

    @pytest.mark.parametrize("numCourses, prerequisites", [
        pytest.param(2,[[1, 0], [1, 0]])
    ])
    def test_bad_request_can_finish_all_pairs_prerequisites_i_UnUnique(self, numCourses, prerequisites):
        assert post_form(data={
            'numCourses': numCourses,
            'prerequisites': ';'.join([','.join(map(str, pair)) for pair in prerequisites])
        }).status_code == 400

    @pytest.mark.parametrize("numCourses, prerequisites", [
        # pytest.param(2, [['0', '0']]),
        pytest.param(2, [[[], []]]),
        pytest.param(2, [[None, None]]),
        pytest.param(2, [[0.5, 0.3]]),
        pytest.param(2, [[True, True]]),
        pytest.param(2, [[b'1', b'1']]),
        pytest.param(2, [[{'numCourses': 1}, {'numCourses': 1}]])
    ])
    def test_bad_request_can_prerequisites_i_isNotArrayOfNumbers(self, numCourses, prerequisites):
        assert post_form(data={
            'numCourses': numCourses,
            'prerequisites': ';'.join([','.join(map(str, pair)) for pair in prerequisites])
        }).status_code == 400

    @pytest.mark.parametrize("numCourses, prerequisites", [
        pytest.param('0', [[1,0]]),
        pytest.param([], [[1,0]]),
        pytest.param(None, [[1,0]]),
        pytest.param(0.5, [[1,0]]),
        pytest.param(True, [[1,0]]),
        pytest.param({'numCourses': 1}, [[1,0]]),
        pytest.param(b'1', [[1,0]]),
        pytest.param((1,), [[1,0]])
    ])
    def test_bad_request_can_numCourses_i_isNotNumber(self, numCourses, prerequisites):
        assert post_form(data={
            'numCourses': numCourses,
            'prerequisites': ';'.join([','.join(map(str, pair)) for pair in prerequisites])
        }).status_code == 400


    def test_bad_request_wrong_form_key(self):
        assert post_form({'test': 'data'}).status_code == 400

    def test_bad_request_extra_form_key_ok(self):
        assert post_form(data = {
            'numCourses': 2,
            'prerequisites': '1,0',
            'test': 'data'
        }).status_code == 200

    def test_bad_request_extra_form_key_result(self):
        assert post_form(data = {
            'numCourses': 2,
            'prerequisites': '1,0',
            'test': 'data'
        }).json()['result']

    def test_request_no_data(self):
        assert post_form({}).status_code == 400