require_relative "lib/crawlora/fortnite/version"

Gem::Specification.new do |spec|
  spec.name = "crawlora-fortnite"
  spec.version = Crawlora::Fortnite::VERSION
  spec.summary = "Fortnite API client for Crawlora (10 endpoints)"
  spec.description = "Ruby client for Crawlora's hosted Fortnite API. Covers public island discovery, genres, rankings, and engagement metrics across 10 endpoints."
  spec.authors = ["Crawlora"]
  spec.license = "MIT"
  spec.required_ruby_version = ">= 2.6"
  spec.files = Dir["lib/**/*.rb", "README.md", "CHANGELOG.md", "LICENSE"]
  spec.require_paths = ["lib"]
  spec.homepage = "https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=fortnite-ruby-homepage"
  spec.metadata = { "source_code_uri" => "https://github.com/Crawlora-org/crawlora-fortnite", "documentation_uri" => "https://github.com/Crawlora-org/crawlora-fortnite/blob/main/ruby/README.md", "rubygems_mfa_required" => "true" }

end
