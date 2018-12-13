require 'mechanize'

class Scrape

  def initialize
    @mechanize = Mechanize.new
    @visited   = []
    @v_titles  = []

    @csv = File.open('keywords-uow.csv', 'a')
  end

  def run(urls)
    scraped_urls = []

    urls.each do |url|
      if !@visited.include?(url)
        begin
          rawpage = @mechanize.get(url)

          rawpage.links.uniq.each do |a|
            scraped_urls << a.href
          end

          page_title = ''

          rawpage.search('title').each do |title|
            page_title = title.text.downcase.strip
          end

          keywords = page_title

          if !page_title.empty? && !keywords.empty? && !@v_titles.include?(page_title)
            puts
            puts "TITLE:    #{page_title}"
            puts "KEYWORDS: #{keywords.join(',')}"

            @csv << %("#{page_title}","#{keywords.join(',').downcase}"\n)
          end

          @v_titles << page_title
        rescue
        end
      end
    end

    @visited += urls
    run(scraped_urls.uniq)
  end

end

@scrape = Scrape.new
@scrape.run([
  'https://www.uow.edu.au/student/'
])
