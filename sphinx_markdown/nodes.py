
import os

from docutils import nodes
import markdown

from sphinx_markdown.extensions.images import StaticImagesExtension
from sphinx_markdown.support import file_read


class MarkdownNode(nodes.raw, nodes.Element):
    """HTML container for markdown contents
    """
    filename = ''
    htmlcontent = ''
    extensions = []

    def load_markdown(self):
        """Save the markdown contents to this node
        """
        text = file_read(self.filename)
        static_dir = os.path.relpath('_static',
                                     start=os.path.dirname(self.filename))
        sphinx_md_ext = StaticImagesExtension(static_dir=static_dir)
        extensions = [sphinx_md_ext]+self.extensions
        self.htmlcontent = markdown.markdown(text, extensions=extensions)

    def astext(self):
        return self.htmlcontent


def visit_markdown_node(document, node):
    document.body.append(node.htmlcontent)


def depart_markdown_node(document_, node_):
    pass
