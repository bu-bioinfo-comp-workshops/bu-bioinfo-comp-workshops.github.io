FROM jekyll/jekyll:4.2.2

WORKDIR /srv/jekyll
COPY Gemfile /srv/jekyll/Gemfile

RUN bundle install

CMD ["bundle", "exec", "jekyll", "serve", "--watch", "--host", "0.0.0.0"]
