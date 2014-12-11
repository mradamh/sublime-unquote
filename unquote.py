import sublime, sublime_plugin
from sublime import Region

class UnquoteCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    v = self.view

    for region in v.sel():
      text = v.substr(region)
      # if the selection starts and ends with matching quotes, just remove them
      # otherwise expand the selection on char each way and try that
      if((text.startswith("'") and text.endswith("'")) or (text.endswith('"') and text.endswith('"')) or (text.endswith('`') and text.endswith('`'))):
        v.erase(edit, Region(region.end() - 1, region.end()))
        v.erase(edit, Region(region.begin(), region.begin() + 1))
      else:
        leftQuoteRegion = Region(region.begin() - 1, region.begin())
        rightQuoteRegion = Region(region.end(), region.end() + 1)
        leftChar = v.substr(leftQuoteRegion)
        rightChar = v.substr(rightQuoteRegion)

        if((leftChar == "'" and rightChar == "'") or (leftChar == '"' and rightChar == '"') or (leftChar == '`' and rightChar == '`')):
          v.erase(edit, rightQuoteRegion);
          v.erase(edit, leftQuoteRegion);
