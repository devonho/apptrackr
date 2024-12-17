package org.devonho.apptrackr.models;

import org.springframework.data.annotation.Id;

public class Application {

	@Id
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

	@Override
	public String toString() {
		return "Job Application [id=" + id + ", title=" + jobListing.getJobTitle() + ", listingURL=" + jobListing.getJobListingURL() + "]";
	}
}