import os
import json
import argparse
from Preprocess.data_preprocess import load_data
from Model.retrieval import voyage_retrieve

def main(question_path, source_path, output_path):
    """
    Main function to load questions, perform retrieval, and save results.

    Args:
        question_path (str): Path to the questions JSON file.
        source_path (str): Path to the directory containing source documents.
        output_path (str): Path to save the retrieval results.
    """
    answer_dict = {"answers": []}
    with open(question_path, 'r') as f:
        qs_ref = json.load(f)

    source_path_finance = os.path.join(source_path, 'finance')
    corpus_dict_finance = load_data(source_path_finance)

    source_path_insurance = os.path.join(source_path, 'insurance')
    corpus_dict_insurance = load_data(source_path_insurance)

    with open(os.path.join(source_path, 'faq/pid_map_content.json'), 'r') as f_s:
        key_to_source_dict = json.load(f_s)
        key_to_source_dict = {int(key): value for key, value in key_to_source_dict.items()}

    for q_dict in qs_ref['questions']:
        if q_dict['category'] == 'finance':
            retrieved = voyage_retrieve(q_dict['query'], q_dict['source'], corpus_dict_finance)
        elif q_dict['category'] == 'insurance':
            retrieved = voyage_retrieve(q_dict['query'], q_dict['source'], corpus_dict_insurance)
        elif q_dict['category'] == 'faq':
            corpus_dict_faq = {key: str(value) for key, value in key_to_source_dict.items() if key in q_dict['source']}
            retrieved = voyage_retrieve(q_dict['query'], q_dict['source'], corpus_dict_faq)
        else:
            raise ValueError("Unknown category in question set")

        answer_dict['answers'].append({"qid": q_dict['qid'], "retrieve": retrieved})

    with open(output_path, 'w', encoding='utf8') as f:
        json.dump(answer_dict, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run retrieval pipeline.')
    parser.add_argument('--question_path', type=str, required=True, help='Path to questions JSON file')
    parser.add_argument('--source_path', type=str, required=True, help='Path to source documents directory')
    parser.add_argument('--output_path', type=str, required=True, help='Path to save retrieval output')

    args = parser.parse_args()
    main(args.question_path, args.source_path, args.output_path)