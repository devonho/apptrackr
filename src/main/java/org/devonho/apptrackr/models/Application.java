package org.devonho.apptrackr.models;

public class Application {

	private String id;
	private JobListing jobListing;

	public Application() {

	}

	public Application(JobListing jobListing) {
		this.jobListing = jobListing;
	}

	public String getId() {
		return id;
	}

  public void setId(String id) {
    this.id = id;
  }

  public JobListing getJobListing() {
    return this.jobListing;
  }

  public void setJobListing(JobListing listing) {
    this.jobListing = listing;
  }

	@Override
	public String toString() {
		return "Job Application [id=" + id + ", title=" + jobListing.getJobTitle() + ", listingURL=" + jobListing.getJobListingURL() + "]";
	}
}