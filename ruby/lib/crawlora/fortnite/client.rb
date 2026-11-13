require "json"
require "net/http"
require "uri"

module Crawlora
  module Fortnite
    module Errors
      class Error < StandardError
        attr_reader :status, :operation_id, :body

        def initialize(message, status: nil, operation_id: nil, body: nil)
          super(message)
          @status, @operation_id, @body = status, operation_id, body
        end
      end
      class ClientError < Error; end
      class ServerError < Error; end
      class NetworkError < Error; end
    end

    OPERATIONS = JSON.parse(<<~'JSON').freeze
      {"fortnite-ecosystem-metric": {"bodyParam": null, "bodyRequired": false, "id": "fortnite-ecosystem-metric", "method": "GET", "params": [{"description": "Bucket size", "enum": ["day", "hour", "minute"], "in": "query", "name": "interval", "required": true, "type": "string", "x-example": "day"}, {"description": "Native metric path variant", "enum": ["in-client-peak-ccu", "in-match-peak-ccu"], "in": "query", "name": "metric", "required": true, "type": "string", "x-example": "in-client-peak-ccu"}, {"description": "Inclusive ISO-8601 start time, within seven days", "in": "query", "name": "from", "type": "string"}, {"description": "Exclusive ISO-8601 end time", "in": "query", "name": "to", "type": "string"}], "path": "/fortnite/ecosystem-metric", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["day", "hour", "minute"], "in": "query", "name": "interval", "required": true, "type": "string"}, {"enum": ["in-client-peak-ccu", "in-match-peak-ccu"], "in": "query", "name": "metric", "required": true, "type": "string"}, {"in": "query", "name": "from", "type": "string"}, {"in": "query", "name": "to", "type": "string"}], "security": ["ApiKeyAuth"]}, "fortnite-ecosystem-metrics": {"bodyParam": null, "bodyRequired": false, "id": "fortnite-ecosystem-metrics", "method": "GET", "params": [{"description": "Bucket size", "enum": ["day", "hour", "minute"], "in": "query", "name": "interval", "required": true, "type": "string", "x-example": "day"}, {"collectionFormat": "csv", "description": "Optional repeatable metric filter", "in": "query", "items": {"enum": ["inMatchPeakCCU", "inClientPeakCCU"], "type": "string"}, "name": "metrics", "type": "array"}, {"description": "Inclusive ISO-8601 start time, within seven days", "in": "query", "name": "from", "type": "string"}, {"description": "Exclusive ISO-8601 end time", "in": "query", "name": "to", "type": "string"}], "path": "/fortnite/ecosystem-metrics", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["day", "hour", "minute"], "in": "query", "name": "interval", "required": true, "type": "string"}, {"collectionFormat": "csv", "enum": ["inMatchPeakCCU", "inClientPeakCCU"], "in": "query", "name": "metrics", "type": "array"}, {"in": "query", "name": "from", "type": "string"}, {"in": "query", "name": "to", "type": "string"}], "security": ["ApiKeyAuth"]}, "fortnite-enums": {"bodyParam": null, "bodyRequired": false, "id": "fortnite-enums", "method": "GET", "params": [], "path": "/fortnite/enums", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "fortnite-genre-rankings": {"bodyParam": null, "bodyRequired": false, "id": "fortnite-genre-rankings", "method": "GET", "params": [{"description": "Genre slug from fortnite_genres", "in": "query", "name": "slug", "required": true, "type": "string"}, {"description": "Hourly point-in-time snapshot, at most seven days old", "in": "query", "name": "at", "type": "string"}, {"description": "Return results after this upstream cursor", "in": "query", "name": "after", "type": "string"}, {"description": "Return results before this upstream cursor", "in": "query", "name": "before", "type": "string"}, {"description": "Upstream page size, 1 through 1000", "in": "query", "name": "size", "type": "integer"}], "path": "/fortnite/genre-rankings", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "slug", "required": true, "type": "string"}, {"in": "query", "name": "at", "type": "string"}, {"in": "query", "name": "after", "type": "string"}, {"in": "query", "name": "before", "type": "string"}, {"in": "query", "name": "size", "type": "integer"}], "security": ["ApiKeyAuth"]}, "fortnite-genres": {"bodyParam": null, "bodyRequired": false, "id": "fortnite-genres", "method": "GET", "params": [], "path": "/fortnite/genres", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "fortnite-island": {"bodyParam": null, "bodyRequired": false, "id": "fortnite-island", "method": "GET", "params": [{"description": "Island code or first-party display name", "in": "query", "name": "code", "required": true, "type": "string"}], "path": "/fortnite/island", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "code", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "fortnite-island-metric": {"bodyParam": null, "bodyRequired": false, "id": "fortnite-island-metric", "method": "GET", "params": [{"description": "Island code or first-party display name", "in": "query", "name": "code", "required": true, "type": "string"}, {"description": "Bucket size", "enum": ["day", "hour", "minute"], "in": "query", "name": "interval", "required": true, "type": "string", "x-example": "day"}, {"description": "Native metric path variant", "enum": ["peak-ccu", "favorites", "minutes-played", "average-minutes-per-player", "recommendations", "unique-players", "plays", "retention"], "in": "query", "name": "metric", "required": true, "type": "string", "x-example": "peak-ccu"}, {"description": "Inclusive ISO-8601 start time, within seven days", "in": "query", "name": "from", "type": "string"}, {"description": "Exclusive ISO-8601 end time", "in": "query", "name": "to", "type": "string"}], "path": "/fortnite/island-metric", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "code", "required": true, "type": "string"}, {"enum": ["day", "hour", "minute"], "in": "query", "name": "interval", "required": true, "type": "string"}, {"enum": ["peak-ccu", "favorites", "minutes-played", "average-minutes-per-player", "recommendations", "unique-players", "plays", "retention"], "in": "query", "name": "metric", "required": true, "type": "string"}, {"in": "query", "name": "from", "type": "string"}, {"in": "query", "name": "to", "type": "string"}], "security": ["ApiKeyAuth"]}, "fortnite-island-metrics": {"bodyParam": null, "bodyRequired": false, "id": "fortnite-island-metrics", "method": "GET", "params": [{"description": "Island code or first-party display name", "in": "query", "name": "code", "required": true, "type": "string"}, {"description": "Optional bucket size", "enum": ["day", "hour", "minute"], "in": "query", "name": "interval", "type": "string"}, {"collectionFormat": "csv", "description": "Optional repeatable metric filter", "in": "query", "items": {"enum": ["averageMinutesPerPlayer", "peakCCU", "favorites", "minutesPlayed", "recommendations", "plays", "uniquePlayers", "retention"], "type": "string"}, "name": "metrics", "type": "array"}, {"description": "Inclusive ISO-8601 start time, within seven days", "in": "query", "name": "from", "type": "string"}, {"description": "Exclusive ISO-8601 end time", "in": "query", "name": "to", "type": "string"}], "path": "/fortnite/island-metrics", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "code", "required": true, "type": "string"}, {"enum": ["day", "hour", "minute"], "in": "query", "name": "interval", "type": "string"}, {"collectionFormat": "csv", "enum": ["averageMinutesPerPlayer", "peakCCU", "favorites", "minutesPlayed", "recommendations", "plays", "uniquePlayers", "retention"], "in": "query", "name": "metrics", "type": "array"}, {"in": "query", "name": "from", "type": "string"}, {"in": "query", "name": "to", "type": "string"}], "security": ["ApiKeyAuth"]}, "fortnite-island-rankings": {"bodyParam": null, "bodyRequired": false, "id": "fortnite-island-rankings", "method": "GET", "params": [{"description": "Island code or first-party display name", "in": "query", "name": "code", "required": true, "type": "string"}, {"description": "Inclusive ISO-8601 start time, within seven days", "in": "query", "name": "from", "type": "string"}, {"description": "Exclusive ISO-8601 end time", "in": "query", "name": "to", "type": "string"}], "path": "/fortnite/island-rankings", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "code", "required": true, "type": "string"}, {"in": "query", "name": "from", "type": "string"}, {"in": "query", "name": "to", "type": "string"}], "security": ["ApiKeyAuth"]}, "fortnite-islands": {"bodyParam": null, "bodyRequired": false, "id": "fortnite-islands", "method": "GET", "params": [{"description": "Return islands after this upstream cursor", "in": "query", "name": "after", "type": "string"}, {"description": "Return islands before this upstream cursor", "in": "query", "name": "before", "type": "string"}, {"description": "Upstream page size, 1 through 1000", "in": "query", "name": "size", "type": "integer"}], "path": "/fortnite/islands", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "after", "type": "string"}, {"in": "query", "name": "before", "type": "string"}, {"in": "query", "name": "size", "type": "integer"}], "security": ["ApiKeyAuth"]}}
    JSON
    OPERATION_IDS = JSON.parse(<<~'JSON').freeze
      ["fortnite-ecosystem-metric", "fortnite-ecosystem-metrics", "fortnite-enums", "fortnite-genre-rankings", "fortnite-genres", "fortnite-island", "fortnite-island-metric", "fortnite-island-metrics", "fortnite-island-rankings", "fortnite-islands"]
    JSON
    OPERATION_COUNT = OPERATION_IDS.length

    class Client
      attr_reader :base_url

      def initialize(api_key: ENV["CRAWLORA_API_KEY"], base_url: "https://api.crawlora.net/api/v1", timeout: 30, user_agent: "crawlora-fortnite-ruby/0.1.0", transport: nil)
        @api_key = api_key
        @base_url = base_url.to_s.sub(%r{/+$}, "")
        @timeout = Float(timeout)
        @user_agent = user_agent
        @transport = transport
        @closed = false
      end

      def request(operation_id, params = {}, response_type: :auto)
        raise Errors::ClientError, "client is closed" if @closed
        operation_id = operation_id.to_s
        operation = OPERATIONS[operation_id]
        raise Errors::ClientError.new("unknown operation: #{operation_id}", operation_id: operation_id) unless operation
        raise Errors::ClientError.new("Crawlora API key is required", operation_id: operation_id) if @api_key.nil? || @api_key.to_s.empty?
        normalized = params.each_with_object({}) { |(key, value), out| out[key.to_s] = value }
        payload = request_body(operation, normalized)
        url = build_url(operation, normalized)
        uri = URI.parse(url)
        request = operation["method"] == "POST" ? Net::HTTP::Post.new(uri) : Net::HTTP::Get.new(uri)
        unless payload.nil?
          request.body = payload
          request["Content-Type"] = "application/json"
        end
        request["x-api-key"] = @api_key
        request["User-Agent"] = @user_agent
        request["Accept"] = operation["produces"].include?("text/plain") ? "application/json, text/plain" : "application/json"
        begin
          if @transport
            response = if operation["method"] == "POST"
              @transport.call(url, request.to_hash, @timeout, "POST", payload)
            else
              @transport.call(url, request.to_hash, @timeout)
            end
            status = Integer(response.fetch(:status) { response.fetch("status") })
            body = response.fetch(:body) { response.fetch("body", "") }
            headers = response.fetch(:headers) { response.fetch("headers", {}) }
            content_type = headers["content-type"] || headers["Content-Type"]
          else
            http = Net::HTTP.new(uri.host, uri.port)
            http.use_ssl = uri.scheme == "https"
            http.open_timeout = @timeout
            http.read_timeout = @timeout
            response = http.start { |connection| connection.request(request) }
            status = response.code.to_i
            body = response.body
            content_type = response["content-type"]
          end
        rescue Timeout::Error, SocketError, SystemCallError, IOError, EOFError, Net::HTTPBadResponse, Net::ProtocolError, OpenSSL::SSL::SSLError => error
          raise Errors::NetworkError.new("Crawlora request failed: #{error.message}", operation_id: operation_id)
        end
        unless status >= 200 && status < 300
          klass = status >= 500 ? Errors::ServerError : Errors::ClientError
          raise klass.new("Crawlora returned HTTP #{status}", status: status, operation_id: operation_id, body: body)
        end
        parse_response(body, content_type, operation, normalized, response_type)
      end

      def close
        @closed = true
      end

      def closed?
        @closed
      end

      def with
        return self unless block_given?
        yield self
      ensure
        close if block_given?
      end

      def self.operation_count
        OPERATION_COUNT
      end

      def self.operation_ids
        OPERATION_IDS
      end

      def self.operations
        OPERATIONS
      end

            define_method('ecosystem_metric') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fortnite-ecosystem-metric', params, response_type: response_type)
      end
      define_method('ecosystem_metrics') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fortnite-ecosystem-metrics', params, response_type: response_type)
      end
      define_method('enums') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fortnite-enums', params, response_type: response_type)
      end
      define_method('genre_rankings') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fortnite-genre-rankings', params, response_type: response_type)
      end
      define_method('genres') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fortnite-genres', params, response_type: response_type)
      end
      define_method('island') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fortnite-island', params, response_type: response_type)
      end
      define_method('island_metric') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fortnite-island-metric', params, response_type: response_type)
      end
      define_method('island_metrics') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fortnite-island-metrics', params, response_type: response_type)
      end
      define_method('island_rankings') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fortnite-island-rankings', params, response_type: response_type)
      end
      define_method('islands') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('fortnite-islands', params, response_type: response_type)
      end

      private

      # POST operations take their JSON body under the body parameter name or "body".
      def request_body(operation, params)
        name = operation["bodyParam"]
        return nil if name.nil?
        value = params.key?(name) ? params[name] : params["body"]
        if value.nil?
          raise Errors::ClientError.new("missing request body: #{name}", operation_id: operation["id"]) if operation["bodyRequired"]
          return nil
        end
        value.is_a?(String) ? value : JSON.generate(value)
      end

      def build_url(operation, params)
        known = operation["params"].map { |param| param["name"] }
        known << "body" if operation["bodyParam"]
        unknown = params.keys - known
        raise Errors::ClientError.new("unknown parameters: #{unknown.join(', ')}", operation_id: operation["id"]) unless unknown.empty?
        path = operation["path"].dup
        operation["params"].select { |param| param["in"] == "path" }.each do |param|
          value = params[param["name"]]
          raise Errors::ClientError.new("missing path parameter: #{param['name']}", operation_id: operation["id"]) if value.nil?
          path.sub!("{" + param["name"] + "}", percent_encode(value.to_s))
        end
        pairs = []
        operation["queryParams"].each do |param|
          name = param["name"]
          value = params.key?(name) ? params[name] : param["default"]
          if value.nil?
            raise Errors::ClientError.new("missing query parameter: #{name}", operation_id: operation["id"]) if param["required"]
            next
          end
          enum_values = param["enum"] || (param["items"] && param["items"]["enum"])
          if enum_values && !(value.is_a?(Array) ? value : [value]).all? { |item| enum_values.map(&:to_s).include?(item.to_s) }
            raise Errors::ClientError.new("invalid value for #{name}", operation_id: operation["id"])
          end
          if value.is_a?(Array)
            format = param["collectionFormat"] || "csv"
            if format == "multi"
              value.each { |item| pairs << [name, scalar(item)] }
            else
              separator = {"csv" => ",", "ssv" => " ", "tsv" => "\t", "pipes" => "|"}[format] || ","
              pairs << [name, value.map { |item| scalar(item) }.join(separator)]
            end
          else
            pairs << [name, scalar(value)]
          end
        end
        query = pairs.map { |name, value| "#{percent_encode(name)}=#{percent_encode(value)}" }.join("&")
        @base_url + path + (query.empty? ? "" : "?" + query)
      end

      def scalar(value)
        value == true ? "true" : (value == false ? "false" : value.to_s)
      end

      def percent_encode(value)
        URI::DEFAULT_PARSER.escape(value.to_s, /[^A-Za-z0-9\-._~]/)
      end

      def parse_response(body, content_type, operation, params, response_type)
        type = response_type.to_s
        raise Errors::ClientError.new("response_type must be auto, json, or text", operation_id: operation["id"]) unless %w[auto json text].include?(type)
        format = operation["params"].find { |param| param["name"] == "format" }
        text_formats = format && format["enum"] ? format["enum"].reject { |value| %w[json application/json].include?(value.to_s.downcase) } : []
        raw_format = params["format"] && text_formats.include?(params["format"].to_s)
        json_format = format && format["enum"] && format["enum"].any? { |value| %w[json application/json].include?(value.to_s.downcase) } && %w[json application/json].include?(params["format"].to_s.downcase)
        is_json = json_format || content_type.to_s.downcase.include?("json") || operation["produces"] == ["application/json"]
        return body if type == "text" || raw_format || (type == "auto" && !is_json)
        JSON.parse(body)
      rescue JSON::ParserError => error
        raise Errors::Error.new("invalid JSON response from Crawlora: #{error.message}", operation_id: operation["id"], body: body)
      end

      public
    end
  end
end
