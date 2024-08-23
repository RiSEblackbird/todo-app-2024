FROM ruby:3.3.4

RUN apt-get update -qq && apt-get install -y nodejs default-mysql-client graphviz

WORKDIR /app

COPY Gemfile Gemfile.lock ./
RUN bundle install
RUN bundle exec rails generate rspec:install

COPY . .

COPY wait-for-it.sh /usr/bin/wait-for-it.sh
RUN chmod +x /usr/bin/wait-for-it.sh

CMD ["rails", "server", "-b", "0.0.0.0"]