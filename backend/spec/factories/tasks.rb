
FactoryBot.define do
  factory :task do
    title { "Sample Task" }
    description { "This is a sample task description" }
    status { "todo" }
    association :user
  end
end
