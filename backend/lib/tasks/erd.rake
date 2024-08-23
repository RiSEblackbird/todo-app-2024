if defined?(RailsERD)
  namespace :erd do
    task :load_models do
      Rails.application.eager_load!
    end

    task :generate => :load_models do
      RailsERD.load_tasks
    end
  end

  desc 'Generate Entity-Relationship Diagram'
  task :erd => 'erd:generate'
end