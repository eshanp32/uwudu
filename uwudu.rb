# (U w U)_/××××××××××××××××××××  Brew tap formula  ××××××××××××××××××××\_(U w U)

class Uwudu < Formula
  desc "your cli todo list manager"
  homepage "https://github.com/eshanp32/uwudu"
  url "https://github.com/eshanp32/uwudu/archive/refs/tags/v0.1.0.tar.gz"
  sha256 "2d674e9153a63ebfd845fc9a142bfffe32d2f8282f232a68139033647ee338b1"
  license "MIT"

  depends_on "python@3.9"

  def install
    virtualenv_install_with_resources
  end

  test do
    assert_match "uwudu", shell_output("#{bin}/uwudu --version")
  end
end