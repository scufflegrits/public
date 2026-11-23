"""Deterministic source checks; these do not establish render or visual correctness."""
import tempfile
import unittest
from pathlib import Path
from audit_mermaid import extract, lint, configuration
from opaque_svg import paint

class AuditChecks(unittest.TestCase):
    def test_section_does_not_use_yaml_comment(self):
        with tempfile.TemporaryDirectory() as out:
            path=Path(out)/'sample.md'
            path.write_text('# Real section\n```mermaid\n---\n# Not a section\nconfig:\n  theme: base\n---\nflowchart LR\n  A["A"]\n```\n')
            blocks=list(extract(path))
            self.assertEqual(blocks[0][1],'Real section')
            self.assertTrue(blocks[0][2].startswith('---\n'))
    def test_named_theme_color(self):
        self.assertEqual(lint('',{'themeVariables':{'primaryColor':'red'}})[0]['check'],'theme-color-format')
    def test_unquoted_yaml_hex(self):
        code='---\nconfig:\n  themeVariables:\n    background: #ffffff\n---\nflowchart LR\n'
        self.assertTrue(lint(code,configuration(code)))
    def test_valid_hex_and_boolean(self):
        self.assertEqual(lint('',{'themeVariables':{'primaryColor':'#ffffff','darkMode':False}}),[])
    def test_duplicate_node(self):
        self.assertTrue(any(x['check']=='duplicate-node-declaration' for x in lint('flowchart LR\n  A["one"]\n  A["two"]\n',{})))
    def test_missing_class(self):
        self.assertTrue(any(x['check']=='missing-class-definition' for x in lint('flowchart LR\n  A["one"]\n  class A nodeMissing\n',{})))
    def test_invalid_reference(self):
        self.assertTrue(any(x['check']=='invalid-class-reference' for x in lint('flowchart LR\n  A["one"]\n  class B nodeX\n  classDef nodeX fill:white\n',{})))
    def test_unmatched_group(self):
        self.assertTrue(any(x['check']=='subgraph-balance' for x in lint('flowchart LR\n  subgraph SG_A["A"]\n',{})))
    def test_opaque_preserves_payload(self):
        source='<svg xmlns="http://www.w3.org/2000/svg" viewBox="-1 -2 100 50"><g id="keep"/></svg>'
        result=paint(source)
        self.assertIn('x="-1" y="-2" width="100" height="50"',result)
        self.assertIn('<g id="keep"/>',result)
        self.assertLess(result.index('data-mermaid-canvas'),result.index('<g'))
    def test_opaque_rejects_transparency(self):
        with self.assertRaises(ValueError):paint('<svg viewBox="0 0 1 1"/>','transparent')

if __name__=='__main__':unittest.main()
