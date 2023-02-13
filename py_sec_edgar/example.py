# -*- coding: utf-8 -*-
from pprint import pprint
import os, sys
import click

import py_sec_edgar.feeds.idx

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import py_sec_edgar.feeds.full_index
from py_sec_edgar.edgar_filing import SecEdgarFiling


@click.command()
@click.option('AAPL', default=True)
@click.option('10-K', default=True)
@click.option('--save_output', default=False)
def main(ticker_list_filter, form_list_filter, save_output):

    py_sec_edgar.feeds.full_index.update_full_index_feed(skip_if_exists=True)

    df_filings_idx = py_sec_edgar.feeds.idx.load_local_idx_filing_list(ticker_list_filter=ticker_list_filter, form_list_filter=form_list_filter)

    for i, filing_json in df_filings_idx.iterrows():

        pprint(filing_json)

        sec_filing = SecEdgarFiling(filing_json)
        sec_filing.download()
        sec_filing.load()
        sec_filing.parse_header(save_output=save_output)
        sec_filing.process_filing(save_output=save_output)

if __name__ == "__main__":

    main()
