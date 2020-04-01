def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--build',      help="Build ID received from Jenkins", default='local')
    args = parser.parse_args()

    style = '''
    <style>
    .passed {
        background-color: #34eb93;
    }
    .failed {
        background-color: #eb4f34;
    }
    </style>
    '''

    errors_html = ""

    detailed_html = ""
    detailed_html += '<h2>Detailed report</h2>\n'
    detailed_html += '<table id="results">\n'
    files = glob.glob(f'reports/*-{args.build}.json')
    for json_file in files:
        try:
            with open(json_file) as fh:
                report = json.load(fh)
            for test in report['tests']:
                if test['outcome'] != 'passed':
                    errors_html += f"{test['outcome']} in {test['nodeid']}<b>"
                    if 'call' in test and 'longrepr' in test['call']:
                        errors_html += f"<pre>{test['call']['longrepr']}</pre>"
                    errors_html += "<p>\n"

                detailed_html += f"""<tr><td>{test['nodeid']}</td><td class="{test['outcome']}">{test['outcome']}</td></tr>\n"""
        except Exception:
            print("Exception")
    detailed_html += '</table>'

    if errors_html:
        errors_html = "<h2>Errors</h2>\n" + errors_html


    html = style + errors_html + detailed_html
    print(html)

main()
