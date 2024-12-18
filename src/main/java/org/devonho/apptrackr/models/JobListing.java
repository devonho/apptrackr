package org.devonho.apptrackr.models;

import java.util.Date;

public class JobListing {
    
	private String jobTitle;
	private String jobListingURL;
  private String jobListingDescription;
  private Date jobListingDate;

  public JobListing() {}

  public JobListing(String jobTitle, String jobListingURL, String jobListingDescription, Date jobListingDate) {
        this.jobTitle = jobTitle;
        this.jobListingURL = jobListingURL;
        this.jobListingDescription = jobListingDescription;
        this.jobListingDate = jobListingDate;
  }

  public String getJobTitle() {
    return jobTitle;
  }  

  public void setJobTitle(String jobTitle) {
    this.jobTitle = jobTitle;
  } 

	public String getJobListingURL() {
		return jobListingURL;
	}

  public void setJobListingURL(String url) {
    this.jobListingURL = url;
  }

  public String getJobListingDescription() {
      return jobListingDescription;
  }

  public void setJobListingDescription(String description) {
    this.jobListingDescription = description;
  }

  public Date getJobListingDate() {
    return jobListingDate;
  }

  public void setJobListingDate(Date date) {
    this.jobListingDate = date;
  }

}
