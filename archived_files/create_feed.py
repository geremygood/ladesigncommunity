try:
  from lxml import etree
  print("running with lxml.etree")
except ImportError:
  try:
    # Python 2.5
    import xml.etree.cElementTree as etree
    print("running with cElementTree on Python 2.5+")
  except ImportError:
    try:
      # Python 2.5
      import xml.etree.ElementTree as etree
      print("running with ElementTree on Python 2.5+")
    except ImportError:
      try:
        # normal cElementTree install
        import cElementTree as etree
        print("running with cElementTree")
      except ImportError:
        try:
          # normal ElementTree install
          import elementtree.ElementTree as etree
          print("running with ElementTree")
        except ImportError:
          print("Failed to import ElementTree from any known place")



root = etree.Element("xml", version="1.0", encoding="utf-8")
rss = etree.SubElement(root, "rss", version="2.0")
channel = etree.SubElement(rss, "channel")


etree.SubElement(channel, "title").text = "LADesign.Community"
etree.SubElement(channel, "description").text = "A list of LS's design community."
etree.SubElement(channel, "link").text = "http://www.ladesign.community"
etree.SubElement(channel, "language").text = "en-us"


tree = etree.ElementTree(root)
tree.write("filename.xml")
