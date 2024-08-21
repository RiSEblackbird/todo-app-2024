require 'rails_helper'

RSpec.describe Task, type: :model do
  describe 'validations' do
    it { should validate_presence_of(:title) }
    it { should validate_presence_of(:status) }
  end

  describe 'associations' do
    it { should belong_to(:user).optional }
  end

  describe 'factory' do
    it 'has a valid factory' do
      expect(build(:task)).to be_valid
    end
  end

  describe 'status' do
    it 'is invalid with an invalid status' do
      task = build(:task, status: 'invalid_status')
      expect(task).not_to be_valid
    end

    it 'is valid with a valid status' do
      %w[todo in_progress done].each do |status|
        task = build(:task, status: status)
        expect(task).to be_valid
      end
    end
  end
end